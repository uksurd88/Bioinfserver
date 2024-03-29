/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2008-10-01 20:49:06 +0200 (Wed, 01 Oct 2008) $
 * $Revision: 9964 $
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

import org.jmol.util.Logger;
import org.jmol.util.TextFormat;
import org.jmol.g3d.*;

import java.awt.Image;
import java.util.BitSet;
import java.util.Enumeration;

public class Echo extends TextShape {

  /*
   * set echo Text.TOP    [Text.LEFT|Text.CENTER|Text.RIGHT]
   * set echo MIDDLE [Text.LEFT|Text.CENTER|Text.RIGHT]
   * set echo BOTTOM [Text.LEFT|Text.CENTER|Text.RIGHT]
   * set echo name   [Text.LEFT|Text.CENTER|Text.RIGHT]
   * set echo name  x-position y-position
   * set echo none  to initiate setting default settings
   * 
   */

  private final static String FONTFACE = "Serif";
  private final static int FONTSIZE = 20;
  private final static short COLOR = Graphics3D.RED;
    
  public void initShape() {
    super.initShape();
    setProperty("target", "top", null);
  }

  public void setProperty(String propertyName, Object value, BitSet bsSelected) {

    if (Logger.debugging) {
      Logger.debug("Echo.setProperty(" + propertyName + "," + value + ")");
    }

    if ("scalereference" == propertyName) {
      if (currentObject != null) {
        float val = ((Float) value).floatValue();
        currentObject.setScalePixelsPerMicron(val == 0 ? 0 : 10000f / val);
      }
      return;
    }

    if ("xyz" == propertyName) {
      if (currentObject != null && viewer.getFontScaling())
        currentObject.setScalePixelsPerMicron(viewer
            .getScalePixelsPerAngstrom() * 10000f);
      // continue on to Object2d setting
    }

    if ("image" == propertyName) {
      Image image = (Image) value;
      if (currentObject == null) {
        if (isAll) {
          Enumeration e = objects.elements();
          while (e.hasMoreElements())
            ((Text) e.nextElement()).setImage(image);
        }
        return;
      }
      ((Text) currentObject).setImage(image);
      return;
    }
    if ("thisID" == propertyName) {
      String target = (String) value;
      currentObject = (Text) objects.get(target);
      if (currentObject == null && TextFormat.isWild(target))
        thisID = target.toUpperCase();
      return;
    }

    if ("hidden" == propertyName) {
      boolean isHidden = ((Boolean) value).booleanValue();
      if (currentObject == null) {
        if (isAll || thisID != null) {
          Enumeration e = objects.elements();
          while (e.hasMoreElements()) {
            Text text = (Text) e.nextElement();
            if (isAll
                || TextFormat.isMatch(text.target.toUpperCase(), thisID, true,
                    true))
              text.hidden = isHidden;
          }
        }
        return;
      }
      ((Text) currentObject).hidden = isHidden;
      return;
    }

    if (Object2d.setProperty(propertyName, value, currentObject))
      return;

    if ("target" == propertyName) {
      thisID = null;
      String target = ((String) value).intern().toLowerCase();
      if (target == "none" || target == "all") {
        // process in Object2dShape
      } else {
        Text text = (Text) objects.get(target);
        if (text == null) {
          int valign = Object2d.VALIGN_XY;
          int halign = Object2d.ALIGN_LEFT;
          if ("top" == target) {
            valign = Object2d.VALIGN_TOP;
            halign = Object2d.ALIGN_CENTER;
          } else if ("middle" == target) {
            valign = Object2d.VALIGN_MIDDLE;
            halign = Object2d.ALIGN_CENTER;
          } else if ("bottom" == target) {
            valign = Object2d.VALIGN_BOTTOM;
          }
          text = new Text(viewer, g3d, g3d.getFont3D(FONTFACE, FONTSIZE),
              target, COLOR, valign, halign, 0);
          text.setAdjustForWindow(true);
          objects.put(target, text);
          if (currentFont != null)
            text.setFont(currentFont);
          if (currentColor != null)
            text.setColix(currentColor);
          if (currentBgColor != null)
            text.setBgColix(currentBgColor);
          if (currentTranslucentLevel != 0)
            text.setTranslucent(currentTranslucentLevel, false);
          if (currentBgTranslucentLevel != 0)
            text.setTranslucent(currentBgTranslucentLevel, true);
        }
        currentObject = text;
        return;
      }
    }
    super.setProperty(propertyName, value, null);
  }

  public Object getProperty(String property, int index) {
    if (property.startsWith("checkID:")) {
      // returns FIRST match
      String key = property.substring(8).toUpperCase();
      boolean isWild = TextFormat.isWild(key);
      Enumeration e = objects.elements();
      while (e.hasMoreElements()) {
        String id = ((Text) e.nextElement()).target.toUpperCase(); 
        if (id.equals(key) || isWild && TextFormat.isMatch(id, key, true, true))
          return id;
      }
    }
    return null;
  }
  public String getShapeState() {
    StringBuffer s = new StringBuffer("\n  set echo off;\n");
    Enumeration e = objects.elements();
    while (e.hasMoreElements()) {
      Text t = (Text) e.nextElement();
      s.append(t.getState());
      if (t.hidden)
        s.append("  set echo " + t.target + " hidden;\n");
    }
    return s.toString();
  }
}
