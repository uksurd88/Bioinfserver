/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2008-06-05 09:23:48 +0200 (Thu, 05 Jun 2008) $
 * $Revision: 9464 $
 *
 * Copyright (C) 2002-2005  The Jmol Development Team
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
package org.jmol.shape;
import org.jmol.g3d.Graphics3D;

public class FrankRenderer extends FontLineShapeRenderer {

  //we render Frank last just for the touch that if there are translucent
  //objects, then it becomes translucent. Just for fun.
  
  // no FrankGenerator
  
  protected void render() {
    Frank frank = (Frank) shape;
    colix = (viewer.isSignedApplet() ? Graphics3D.RED : Graphics3D.GRAY);
    if (isGenerator || !viewer.getShowFrank()
        || !g3d.setColix(Graphics3D.getColixTranslucent(colix,
            g3d.haveTranslucentObjects(), 0.5f)))
      return;
    imageFontScaling = viewer.getImageFontScaling();
    frank.getFont(imageFontScaling);
    int dx = (int) (frank.frankWidth + Frank.frankMargin * imageFontScaling);
    int dy = frank.frankDescent;
    g3d.drawStringNoSlab(frank.frankString, frank.font3d,
        g3d.getRenderWidth() - dx, g3d.getRenderHeight() - dy, 0);
  }
}
