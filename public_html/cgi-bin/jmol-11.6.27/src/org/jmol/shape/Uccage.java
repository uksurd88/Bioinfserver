/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2007-05-22 14:48:05 +0200 (Tue, 22 May 2007) $
 * $Revision: 7806 $
 *
 * Copyright (C) 2003-2006  Miguel, Jmol Development, www.jmol.org
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
package org.jmol.shape;

public class Uccage extends FontLineShape {

  public String getShapeState() {
    if (modelSet.getCellInfos() == null)
      return "";
    return super.getShapeState();
  }

  public void initShape() {
    super.initShape();
    myType = "unitcell";
  }
}
