/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2006-08-27 21:07:49 -0500 (Sun, 27 Aug 2006) $
 * $Revision: 5420 $
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
package org.jmol.adapter.readers.more;

import org.jmol.adapter.smarter.*;


import java.io.BufferedReader;
import java.util.Hashtable;


/**
 * Reads Mopac 2007 GRAPHF output files
 *
 * @author Bob Hanson <hansonr@stolaf.edu>
 * 
 */
public class MopacGraphfReader extends MopacDataReader {
    
  int[] atomicNumbers;
  int atomCount;
  
 public AtomSetCollection readAtomSetCollection(BufferedReader reader) {

    this.reader = reader;
    atomSetCollection = new AtomSetCollection("mopacGraphf");
    //frameInfo = null;
    try {
      readAtoms();
      readSlaterBasis();
      readMOs(false);
      if (readKeywords())
        readMOs(true);
    } catch (Exception e) {
      return setError(e);
    }
    return atomSetCollection;
  }
    
  void readAtoms() throws Exception {
    atomSetCollection.newAtomSet();
    atomCount = parseInt(readLine());
    atomicNumbers = new int[atomCount];
    for (int i = 0; i < atomCount; i++) {
      readLine();
      atomicNumbers[i] = parseInt(line.substring(0, 4));
      Atom atom = atomSetCollection.addNewAtom();
      atom.x = parseFloat(line.substring(4, 17));
      atom.y = parseFloat(line.substring(17, 29));
      atom.z = parseFloat(line.substring(29, 41));
      if (line.length() > 41)
        atom.partialCharge = parseFloat(line.substring(41));
      atom.elementSymbol = AtomSetCollectionReader.getElementSymbol(atomicNumbers[i]);
      //System.out.println(atom.elementSymbol + " " + atom.x + " " + atom.y + " " + atom.z);
    }
  }
  
  /*
   *  see http://openmopac.net/manual/graph.html
   *  
   Block 1, 1 line: Number of atoms (5 characters), plain text: "MOPAC-Graphical data"
   Block 2, 1 line per atom: Atom number (4 characters), Cartesian coordinates (3 sets of 12 characters)
   Block 3, 1 line per atom: Orbital exponents for "s", "p", and "d" Slater orbitals. (3 sets of 11 characters)
   Block 4, number of orbitals squared, All the molecular orbital coefficients in the order M.O. 1, M.O.2, etc. (5 data per line, 15 characters per datum, FORTRAN format: 5d15.8)
   Block 4, inverse-square-root of overlap matrix, (number of orbitals*(number of orbitals+1))/2.
   4 MOPAC-Graphical data
   
   8    0.0000000   0.0000000   0.0000000
   6    1.2108153   0.0000000   0.0000000
   1    1.7927832   0.9304938   0.0000000
   1    1.7927832  -0.9304938   0.0000000

   
   0         1         2         3         4
   01234567890123456789012345678901234567890
   

   5.4217510  2.2709600  0.0000000
   2.0475580  1.7028410  0.0000000
   1.2686410  0.0000000  0.0000000
   1.2686410  0.0000000  0.0000000
   */

  void readSlaterBasis() throws Exception {
    /*
     * We have two data structures for each slater, using the WebMO format: 
     * 
     * int[] slaterInfo[] = {iatom, a, b, c, d}
     * float[] slaterData[] = {zeta, coef}
     * 
     * where
     * 
     *  psi = (coef)(x^a)(y^b)(z^c)(r^d)exp(-zeta*r)
     * 
     * except: a == -2 ==> z^2 ==> (coef)(2z^2-x^2-y^2)(r^d)exp(-zeta*r)
     *    and: b == -2 ==> (coef)(x^2-y^2)(r^d)exp(-zeta*r)
     */
    nOrbitals = 0;
    float[] values = new float[3];
    for (int iAtom = 0; iAtom < atomCount; iAtom++) {
      getTokensFloat(readLine(), values, 3);
      int atomicNumber = atomicNumbers[iAtom];
      float zeta;
      if ((zeta = values[0]) != 0) {
        //s
        addSlater(iAtom, 0, 0, 0, MopacData.getNPQs(atomicNumber) - 1, zeta,
            MopacData.getMopacConstS(atomicNumber, zeta));
      }
      if ((zeta = values[1]) != 0) {
        int d = MopacData.getNPQp(atomicNumber) - 2;
        float coef = MopacData.getMopacConstP(atomicNumber, zeta);
        addSlater(iAtom, 1, 0, 0, d, zeta, coef);
        addSlater(iAtom, 0, 1, 0, d, zeta, coef);
        addSlater(iAtom, 0, 0, 1, d, zeta, coef);
      }
      if ((zeta = values[2]) != 0) {
        int d = MopacData.getNPQd(atomicNumber) - 3;
        float coef = MopacData.getMopacConstD(atomicNumber, zeta);
        int dpt = 0;
        for (int i = 0; i < 5; i++)
          addSlater(iAtom, dValues[dpt++], dValues[dpt++], dValues[dpt++], d,
              zeta, coef * MopacData.getFactorD(i));
      }
    }
    nOrbitals = intinfo.size();
    setSlaters();
  }

  float[][] invMatrix;
  
  void readMOs(boolean isBeta) throws Exception {

    // read mo coefficients

    //  (5 data per line, 15 characters per datum, FORTRAN format: 5d15.8)

    float[][] list = new float[nOrbitals][nOrbitals];
    for (int iMo = 0; iMo < nOrbitals; iMo++) {
      int n = -1;
      for (int i = 0; i < nOrbitals; i++) {
        if ((n = (n + 1) % 5) == 0)
          readLine();
        list[iMo][i] = parseFloat(line.substring(n * 15, (n + 1) * 15));
      }
    }
    if (!isBeta) {
      // read lower triangle of symmetric inverse sqrt matrix and multiply
      invMatrix = new float[nOrbitals][nOrbitals];
      for (int iMo = 0; iMo < nOrbitals; iMo++) {
        int n = -1;
        for (int i = 0; i < iMo + 1; i++) {
          if ((n = (n + 1) % 5) == 0)
            readLine();
          invMatrix[iMo][i] = invMatrix[i][iMo] = parseFloat(line.substring(
              n * 15, (n + 1) * 15));
        }
      }
    }
    float[][] list2 = new float[nOrbitals][nOrbitals];
    for (int i = 0; i < nOrbitals; i++)
      for (int j = 0; j < nOrbitals; j++) {
        for (int k = 0; k < nOrbitals; k++)
          list2[i][j] += (list[i][k] * invMatrix[k][j]);
        if (Math.abs(list2[i][j]) < MIN_COEF)
          list2[i][j] = 0;
      }
    /*
     System.out.println("MO coefficients: ");
     for (int i = 0; i < nOrbitals; i++) {
     System.out.print((i + 1) + ": ");
     for (int j = 0; j < nOrbitals; j++)
     System.out.print(" " + list2[i][j]);
     System.out.println();
     }
     */

    // read MO energies and occupancies, and fill "coefficients" element
    
    float[] values = new float[2];
    for (int iMo = 0; iMo < nOrbitals; iMo++) {
      Hashtable mo = new Hashtable();
      getTokensFloat(readLine(), values, 2);
      mo.put("energy", new Float(values[0]));
      mo.put("occupancy", new Float(values[1]));
      mo.put("coefficients", list2[iMo]);
      if (isBeta)
        mo.put("type", "beta");
      orbitals.addElement(mo);
    }
    setMOs("eV");
  }
    
  private boolean readKeywords() throws Exception {
    if (readLine() == null || line.indexOf(" Keywords:") < 0)
      return false;
    moData.put("calculationType", line.substring(11).trim());
    boolean isUHF = (line.indexOf("UHF") >= 0);
    if (isUHF)
      for (int i = orbitals.size(); --i >= 0;)
        ((Hashtable)orbitals.get(i)).put("type", "alpha");
    return isUHF;
  }
}
