/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2006-10-22 14:12:46 -0500 (Sun, 22 Oct 2006) $
 * $Revision: 5999 $
 *
 * Copyright (C) 2003-2005  Miguel, Jmol Development, www.jmol.org
 *
 * Contact: miguel@jmol.org
 *
 *  This library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public
 *  License as published by the Free Software Foundation; either
 *  version 2.1 of the License, or (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public
 *  License along with this library; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 */

package org.jmol.adapter.readers.molxyz;

import org.jmol.adapter.smarter.*;


import org.jmol.api.JmolAdapter;
import org.jmol.util.Logger;

import java.io.BufferedReader;

/**
 * A reader for MDLI mol and sdf files.
 *<p>
 * <a href='http://www.mdli.com/downloads/public/ctfile/ctfile.jsp'>
 * http://www.mdli.com/downloads/public/ctfile/ctfile.jsp
 * </a>
 *<p>
 *
 * also: http://www.mdl.com/downloads/public/ctfile/ctfile.pdf
 *
 * simple symmetry extension via load command:
 * 9/2006 hansonr@stolaf.edu
 * 
 *  setAtomCoord(atom, x, y, z)
 *  applySymmetry()
 *  
 */
public class MolReader extends AtomSetCollectionReader {

  String header = "";
 public AtomSetCollection readAtomSetCollection(BufferedReader reader) {
    atomSetCollection = new AtomSetCollection("mol");
    this.reader = reader;
    boolean iHaveAtoms = false;
    try {
      while (readLine() != null) {
        if (line.startsWith("$MDL")) {
          processRgHeader();
          discardLinesUntilStartsWith("$CTAB");
          processCtab();
        } else {
          if (++modelNumber != desiredModelNumber && desiredModelNumber > 0) {
            if (iHaveAtoms)
              break;
            flushLines();
            continue;
          }
          iHaveAtoms = true;
          processMolSdHeader();
          processCtab();
        }
        flushLines();
      }
    } catch (Exception e) {
      return setError(e);
    }
    return atomSetCollection;
  }
  
  void processMolSdHeader() throws Exception {
    /* 
     * obviously we aren't being this strict, but for the record:
     *  
     * from ctfile.pdf (October 2003):
     * 
     * Line 1: Molecule name. This line is unformatted, but like all 
     * other lines in a molfile may not extend beyond column 80. 
     * If no name is available, a blank line must be present.
     * Caution: This line must not contain any of the reserved 
     * tags that identify any of the other CTAB file types 
     * such as $MDL (RGfile), $$$$ (SDfile record separator), 
     * $RXN (rxnfile), or $RDFILE (RDfile headers). 
     * 
     * Line 2: This line has the format:
     * IIPPPPPPPPMMDDYYHHmmddSSssssssssssEEEEEEEEEEEERRRRRR
     * (FORTRAN: A2<--A8--><---A10-->A2I2<--F10.5-><---F12.5--><-I6-> )
     * User's first and last initials (l), program name (P), 
     * date/time (M/D/Y,H:m), dimensional codes (d), scaling factors (S, s), 
     * energy (E) if modeling program input, internal 
     * registry number (R) if input through MDL form. A blank line can be 
     * substituted for line 2. If the internal registry number is more than 
     * 6 digits long, it is stored in an M REG line (described in Chapter 3). 
     * 
     * Line 3: A line for comments. If no comment is entered, a blank line 
     * must be present.
     */

    String thisDataSetName = line;
    header += line + "\n";
    atomSetCollection.setCollectionName(line);
    readLine();
    if (line == null)
      return;
    header += line + "\n";
    //line 3: comment
    readLine();
    if (line == null)
      return;
    header += line + "\n";
    checkLineForScript();
    atomSetCollection.setAtomSetCollectionAuxiliaryInfo("fileHeader", header);
    newAtomSet(thisDataSetName);
  }

  void processRgHeader() throws Exception {
    /*
     * from ctfile.pdf:
     * 
     * $MDL REV 1 date/time
     * $MOL
     * $HDR
     * [Molfile Header Block (see Chapter 4) = name, pgm info, comment]
     * $END HDR
     * $CTAB
     * [Ctab Block (see Chapter 2) = count + atoms + bonds + lists + props]
     * $END CTAB
     * $RGP
     * rrr [where rrr = Rgroup number]
     * $CTAB
     * [Ctab Block]
     * $END CTAB
     * $END RGP
     * $END MOL
     */

    while (readLine() != null && !line.startsWith("$HDR")) {
    }
    if (line == null) {
      Logger.warn("$HDR not found in MDL RG file");
      return;
    }
    readLine();
    processMolSdHeader();
  }

  void processCtab() throws Exception {
    readLine();
    if (line == null)
      return;
    int atomCount = parseInt(line, 0, 3);
    int bondCount = parseInt(line, 3, 6);
    int atom0 = atomSetCollection.getAtomCount();
    readAtoms(atomCount);
    readBonds(atom0, bondCount);
    applySymmetry();
  }

  void flushLines() throws Exception {
    while (readLine() != null && !line.startsWith("$$$$")) {
      //flush
    }
  }

  private final static String isotopeMap0 = "H1 H2 ";
  private final static String isotopeMap1 = "D  T  ";
  void readAtoms(int atomCount) throws Exception {
    for (int i = 0; i < atomCount; ++i) {
      readLine();
      String elementSymbol = "";
      if (line.length() > 34) {
        elementSymbol = line.substring(31, 34).trim().intern();
      } else {
        // deal with older Mol format where nothing after the symbol is used
        elementSymbol = line.substring(31).trim().intern();
      }
      float x = parseFloat(line, 0, 10);
      float y = parseFloat(line, 10, 20);
      float z = parseFloat(line, 20, 30);
      int charge = 0;
      if (line.length() >= 39) {
        int code = parseInt(line, 36, 39);
        if (code >= 1 && code <= 7)
          charge = 4 - code;
        code = parseInt(line, 34, 36);
        if (code != 0 && code >= -3 && code <= 4) {
          int ptr = isotopeMap0.indexOf(elementSymbol + code);
          if (ptr >= 0)
            elementSymbol = isotopeMap1.substring(ptr, ptr + 3).trim();
          else if (elementSymbol=="C")
            elementSymbol = (12 + code) + "C";
          else if (elementSymbol=="N")
            elementSymbol = (14 + code) + "N";
        }
      }
      Atom atom = atomSetCollection.addNewAtom();
      atom.elementSymbol = elementSymbol;
      atom.formalCharge = charge;
      setAtomCoord(atom, x, y, z);
    }
  }

  void readBonds(int atom0, int bondCount) throws Exception {
    for (int i = 0; i < bondCount; ++i) {
      readLine();
      int atomIndex1 = parseInt(line, 0, 3);
      int atomIndex2 = parseInt(line, 3, 6);
      int order = parseInt(line, 6, 9);
      switch (order) {
      case 1:
      case 2:
      case 3:
        break;
      case 4:
        order = JmolAdapter.ORDER_AROMATIC;
        break;
      case 5:
        order = JmolAdapter.ORDER_PARTIAL12;
        break;
      case 6:
        order = JmolAdapter.ORDER_AROMATIC_SINGLE;
        break;
      case 7:
        order = JmolAdapter.ORDER_AROMATIC_DOUBLE;
        break;
      case 8:
        order = JmolAdapter.ORDER_PARTIAL01;
        break;
      }
      atomSetCollection
          .addBond(new Bond(atom0 + atomIndex1 - 1, atom0 + atomIndex2 - 1, order));
    }
  }
}
