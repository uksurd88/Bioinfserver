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
package org.jmol.adapter.readers.xml;

import org.jmol.adapter.smarter.*;


import java.io.BufferedReader;
import java.util.HashMap;

import netscape.javascript.JSObject;

import org.jmol.api.JmolAdapter;
import org.xml.sax.XMLReader;

/**
 * A crude ArgusLab .agl file Reader - http://www.planaria-software.com/
 * 
 * Use this reader as a template for adding new XML readers.
 * 
 */

public class XmlArgusReader extends XmlReader {

  /*
   * Enter any implemented field names in the 
   * implementedAttributes array. It is for when the XML 
   * is already loaded in the DOM of an XML page.
   * 
   */

  String[] argusImplementedAttributes = { 
      "order", //bond
  };

  String[] keepCharsList = { 
      "name", "x", "y", "z", "formalchg", "atomkey", "atsym", 
  };

  String atomName1;
  String atomName2;
  int bondOrder;

  // this param is used to keep track of the parent element type
  int elementContext;
  final static int UNSET = 0;
  final static int MOLECULE = 1;
  final static int ATOM = 2;
  final static int BOND = 3;

  XmlArgusReader() {
  }

  XmlArgusReader(XmlReader parent, AtomSetCollection atomSetCollection, BufferedReader reader,
      XMLReader xmlReader) {
    this.parent = parent;
    this.reader = reader;
    this.atomSetCollection = atomSetCollection;
    new ArgusHandler(xmlReader);
    parseReaderXML(xmlReader);
  }

  XmlArgusReader(XmlReader parent, AtomSetCollection atomSetCollection, JSObject DOMNode) {
    this.parent = parent;
    this.atomSetCollection = atomSetCollection;
    implementedAttributes = argusImplementedAttributes;
    ((ArgusHandler) (new ArgusHandler())).walkDOMTree(DOMNode);
  }

  public void processStartElement(String namespaceURI, String localName, String qName,
                           HashMap atts) {
    //System.out.println("open " + localName);
    for (int i = keepCharsList.length; --i >= 0;)
      if (keepCharsList[i].equals(localName)) {
        setKeepChars(true);
        break;
      }

    if ("molecule".equals(localName)) {
      atomSetCollection.newAtomSet();
      return;
    }
    if ("atom".equals(localName)) {
      elementContext = ATOM;
      atom = new Atom();
      return;
    }
    if ("bond".equals(localName)) {
      elementContext = BOND;
      atomName1 = null;
      atomName2 = null;
      bondOrder = parseBondToken((String) atts.get("order"));
      return;
    }
  }

  int parseBondToken(String str) {
    float floatOrder = parseFloat(str);
    if (Float.isNaN(floatOrder) && str.length() >= 1) {
      str = str.toUpperCase();
      switch (str.charAt(0)) {
      case 'S':
        return 1;
      case 'D':
        return 2;
      case 'T':
        return 3;
      case 'A':
        return JmolAdapter.ORDER_AROMATIC;
      }
      return parseInt(str);
    }
    if (floatOrder == 1.5)
      return JmolAdapter.ORDER_AROMATIC;
    if (floatOrder == 2)
      return 2;
    if (floatOrder == 3)
      return 3;
    return 1;
  }

  public void processEndElement(String uri, String localName, String qName) {
    //System.out.println("close " + localName);
    if (chars != null && chars.length() > 0
        && chars.charAt(chars.length() - 1) == '\n')
      chars = chars.substring(0, chars.length() - 1);
    if ("molecule".equals(localName)) {
      // end-of-molecule operations could be here
      elementContext = UNSET;
      return;
    }
    if ("atom".equals(localName)) {
      if (atom.elementSymbol != null && !Float.isNaN(atom.z)) {
        atomSetCollection.addAtomWithMappedName(atom);
      }
      atom = null;
      elementContext = UNSET;
      return;
    }
    if ("bond".equals(localName)) {
      if (atomName2 != null)
        atomSetCollection.addNewBond(atomName1, atomName2, bondOrder);
      elementContext = UNSET;
      return;
    }

    // contextual assignments 

    if (elementContext == MOLECULE) {
      if ("name".equals(localName)) {
        atomSetCollection.setAtomSetName(chars);
        setKeepChars(false);
      }
      return;
    }
    if (atom != null && elementContext == ATOM) {
      if ("x".equals(localName)) {
        atom.x = parseFloat(chars);
      } else if ("y".equals(localName)) {
        atom.y = parseFloat(chars);
        return;
      } else if ("z".equals(localName)) {
        atom.z = parseFloat(chars);
        return;
      } else if ("atsym".equals(localName)) {
        atom.elementSymbol = chars;
        return;
      } else if ("formalchg".equals(localName)) {
        atom.formalCharge = parseInt(chars);
      } else if ("atomkey".equals(localName)) {
        atom.atomName = chars;
      }
      setKeepChars(false);
      return;
    }
    if (elementContext == BOND) {
      if ("atomkey".equals(localName)) {
        if (atomName1 == null)
          atomName1 = chars;
        else
          atomName2 = chars;
        setKeepChars(false);
      }
      return;
    }
  }

  class ArgusHandler extends JmolXmlHandler {

    ArgusHandler() {
    }

    ArgusHandler(XMLReader xmlReader) {
      setHandler(xmlReader, this);
    }
  }
}
