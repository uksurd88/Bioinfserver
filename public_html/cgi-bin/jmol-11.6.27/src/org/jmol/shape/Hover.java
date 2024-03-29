/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2008-08-06 07:54:53 +0200 (Wed, 06 Aug 2008) $
 * $Revision: 9674 $
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

import org.jmol.g3d.*;
import org.jmol.util.Escape;
import org.jmol.util.Logger;

import java.util.BitSet;
import java.util.Hashtable;

import javax.vecmath.Point3i;

public class Hover extends TextShape {

  private final static String FONTFACE = "SansSerif";
  private final static String FONTSTYLE = "Plain";
  private final static int FONTSIZE = 12;

  Text hoverText;
  int atomIndex = -1;
  Point3i xy;
  String text;
  String labelFormat = "%U";
  String[] atomFormats;

  public void initShape() {
    super.initShape();
    isHover = true;
    Font3D font3d = g3d.getFont3D(FONTFACE, FONTSTYLE, FONTSIZE);
    short bgcolix = Graphics3D.getColix("#FFFFC3"); // 255, 255, 195
    short colix = Graphics3D.BLACK;
    currentObject = hoverText = new Text(g3d, font3d, null, colix, bgcolix, 0, 0,
        1, Integer.MIN_VALUE, Object2d.ALIGN_LEFT, 0);
    hoverText.setAdjustForWindow(true);
  }

  public void setProperty(String propertyName, Object value, BitSet bsSelected) {

    if (Logger.debugging) {
      Logger.debug("Hover.setProperty(" + propertyName + "," + value + ")");
    }

    if ("target" == propertyName) {
      if (value == null)
        atomIndex = -1;
      else {
        atomIndex = ((Integer) value).intValue();
        viewer
            .setStatusAtomHovered(atomIndex, viewer.getAtomInfoXYZ(atomIndex, false));
      }
      return;
    }

    if ("text" == propertyName) {
      text = (String) value;
      if (text != null && text.length() == 0)
        text = null;
      return;
    }

    if ("atomLabel" == propertyName) {
      String text = (String) value;
      if (text != null && text.length() == 0)
        text = null;
      int count = viewer.getAtomCount();
      if (atomFormats == null)
        atomFormats = new String[count];
      for (int i = count; --i >= 0;)
        if (bsSelected.get(i))
          atomFormats[i] = text;
      return;
    }

    if ("xy" == propertyName) {
      xy = (Point3i) value;
      return;
    }

    if ("label" == propertyName) {
      labelFormat = (String) value;
      if (labelFormat != null && labelFormat.length() == 0)
        labelFormat = null;
      return;
    }

    if (propertyName == "deleteModelAtoms") {
      atomIndex = -1;
      return;
    }
    
    super.setProperty(propertyName, value, null);

  }

  public String getShapeState() {
    Hashtable temp = new Hashtable();
    int atomCount = viewer.getAtomCount();
    if (atomFormats != null)
      for (int i = atomCount; --i >= 0;)
        if (atomFormats[i] != null)
          setStateInfo(temp, i, "set hoverLabel " + Escape.escape(atomFormats[i]));
    return "\n  hover " + Escape.escape((labelFormat == null ? "" : labelFormat)) 
    + ";\n" + getShapeCommands(temp, null, atomCount);
  }
}
