/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2006-10-15 17:34:01 -0500 (Sun, 15 Oct 2006) $
 * $Revision: 5957 $
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

import org.jmol.adapter.readers.cifpdb.PdbReader;

/**
 * PQR file reader.
 *
 *<p>
 * <a href='http://www.rcsb.org'>
 * http://www.rcsb.org
 * </a>
 *
 * @author Miguel, Egon, and Bob (hansonr@stolaf.edu)
 * 
 * symmetry added by Bob Hanson:
 * 
 *  setFractionalCoordinates()
 *  setSpaceGroupName()
 *  setUnitCell()
 *  initializeCartesianToFractional();
 *  setUnitCellItem()
 *  setAtomCoord()
 *  applySymmetry()
 *  
 */

public class PqrReader extends PdbReader {
  protected String fileType = "Pqr"; 
  
  protected int readOccupancy() {
    return 100;
  }

  protected float readBFactor() {
    return Float.MAX_VALUE; 
  }
  
  protected float readPartialCharge() {
    return parseFloat(line, 55, 62);
  }
  
  protected float readRadius() {
    return parseFloat(line, 63, 69);
  }
  

}

