/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2007-11-23 12:49:25 -0600 (Fri, 23 Nov 2007) $
 * $Revision: 8655 $
 *
 * Copyright (C) 2003-2005  The Jmol Development Team
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

package org.jmol.minimize;

import java.util.Vector;

import org.jmol.modelset.Atom;

public class MinAtom {

  int index;
  public Atom atom;
  public double[] coord = new double[3];
  public double[] force = new double[3];
  public Vector bonds = new Vector();
  public int nBonds;
  
  public String type;
  int[] bondedAtoms;
  
  MinAtom(int index, Atom atom, double[] coord, String type) {
    this.index = index;
    this.atom = atom;
    this.coord = coord;
    this.type = type;
  }

  void set() {
    coord[0] = atom.x;
    coord[1] = atom.y;
    coord[2] = atom.z;
  }

  public MinBond getBondTo(int iAtom) {
    getBondedAtomIndexes();
    for (int i = 0; i < nBonds; i++)
      if (bondedAtoms[i] == iAtom)
        return (MinBond) bonds.elementAt(i);
    return null;
  }
  
  public int[] getBondedAtomIndexes() {
    if (bondedAtoms == null) {
      bondedAtoms = new int[nBonds];
      for (int i = nBonds; --i >= 0;)
        bondedAtoms[i] = ((MinBond) bonds.elementAt(i)).getOtherAtom(index);
    }
    return bondedAtoms;
  }

  public String getIdentity() {
    return atom.getInfo();
  }

}
