/* $RCSfile$
 * $Author: egonw $
 * $Date: 2005-11-10 09:52:44 -0600 (Thu, 10 Nov 2005) $
 * $Revision: 4255 $
 *
 * Copyright (C) 2004-2005  The Jmol Development Team
 *
 * Contact: jmol-developers@lists.sf.net
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

package org.jmol.adapter.readers.more;

import org.jmol.adapter.smarter.*;


import org.jmol.api.JmolAdapter;
import java.io.BufferedReader;

/**
 * Support for .hin, HyperChem's native file format.
 * http://www.hyper.com
 * <p />
 * Record format is:
 * <code>
 * atom 1 - C ** - -0.06040 0.00000 0.00000 0.00000 3 2 a 6 a 38 s
 * ...
 * atom 67 - H ** - 0.17710 -7.10260 -3.74840 2.24660 1 34 s
 * endmol 1
 * </code>
 * interesting fields are partialCharge, x, y, z, bondCount<br />
 * bonds are atom number and s/d/t/a for single/double/triple/aromatic
 */
public class HinReader extends AtomSetCollectionReader {
  
 public AtomSetCollection readAtomSetCollection(BufferedReader reader) {
    this.reader = reader;
    atomSetCollection = new AtomSetCollection("hin");
    try {
      readAtoms();
    } catch (Exception e) {
      return setError(e);
    }
    return atomSetCollection;
  }
  
  int atomIndex;
  int baseAtomIndex;

  void readAtoms() throws Exception {

    while (readLine() != null ) {
      if (line.length() == 0 || line.charAt(0) == ';') // comment
        continue;
      if (line.startsWith("mol ")) // we have reached the start of a molecule
        processMol();
      else if (line.startsWith("atom "))
        processAtom();
      else if (line.startsWith("endmol "))
        processEndmol();
    }
  }

  void processMol() throws Exception {
    atomSetCollection.newAtomSet();
    String molName = getMolName();
    atomSetCollection.setAtomSetName(molName);
    atomIndex = 0;
    baseAtomIndex = atomSetCollection.getAtomCount();
  }

  String getMolName() {
    parseToken(line);
    parseToken();
    return parseToken();
  }

  void processAtom() throws Exception {

    int fileAtomNumber = parseInt(line, 5);
    if (fileAtomNumber - 1 != atomIndex) {
      throw new Exception ("bad atom number sequence ... expected:" +
        (atomIndex + 1) + " found:" + fileAtomNumber);
    }

    Atom atom = atomSetCollection.addNewAtom();
    parseToken(); // discard
    atom.elementSymbol = parseToken();
    parseToken(); // discard
    parseToken(); // discard
    atom.partialCharge = parseFloat();
    atom.x = parseFloat();
    atom.y = parseFloat();
    atom.z = parseFloat();
    
    int bondCount = parseInt();
    for (int i = 0; i < bondCount; ++i) {
      int otherAtomNumber = parseInt();
      String bondTypeToken = parseToken();
      if (otherAtomNumber > atomIndex)
        continue;
      int bondOrder;
      switch(bondTypeToken.charAt(0)) {
      case 's': 
        bondOrder = 1;
        break;
      case 'd': 
        bondOrder = 2;
        break;
      case 't': 
        bondOrder = 3;
        break;      
      case 'a':
        bondOrder = JmolAdapter.ORDER_AROMATIC;
        break;
      default:
        throw new Exception ("unrecognized bond type:" + bondTypeToken +
          " atom #" + fileAtomNumber);
      }
      atomSetCollection.addNewBond(baseAtomIndex + atomIndex,
                       baseAtomIndex + otherAtomNumber - 1,
                       bondOrder);
    }
    ++atomIndex;
  }

  void processEndmol() {
  }
}
