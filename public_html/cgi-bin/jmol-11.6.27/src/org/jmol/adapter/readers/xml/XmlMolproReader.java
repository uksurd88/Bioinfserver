/* $RCSfile$
 * $Author: hansonr $
 * $Date: 2006-09-12 00:46:22 -0500 (Tue, 12 Sep 2006) $
 * $Revision: 5501 $
 *
 * Copyright (C) 2003-2005  Miguel, Jmol Development, www.jmol.org
 * Copyright (C) 2005  Peter Knowles
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
import org.xml.sax.*;

/**
 * A Molpro 2005 reader
 */

public class XmlMolproReader extends XmlCmlReader {

  /*
   * Enter any implemented field names in the 
   * implementedAttributes array. It is for when the XML 
   * is already loaded in the DOM of an XML page.
   * 
   */

  static String[] molProImplementedAttributes = { "id", "length", "type", //general
      "x3", "y3", "z3", "elementType", //atoms
      "name", //variable
      "groups", "cartesianLength", "primitives", // basisSet and
      "minL", "maxL", "angular", "contractions", //   basisGroup
      "occupation", "energy", "symmetryID", // orbital 
      "wavenumber", "units", // normalCoordinate
  };

  XmlMolproReader(XmlReader parent, AtomSetCollection atomSetCollection, BufferedReader reader, XMLReader xmlReader) {
    this.parent = parent;
    this.reader = reader;
    this.atomSetCollection = atomSetCollection;
    new MolproHandler(xmlReader);
    parseReaderXML(xmlReader);
  }

  XmlMolproReader(XmlReader parent, AtomSetCollection atomSetCollection, JSObject DOMNode) {
    this.parent = parent;
    this.atomSetCollection = atomSetCollection;
    implementedAttributes = molProImplementedAttributes;
    ((MolproHandler) (new MolproHandler())).walkDOMTree(DOMNode);
  }

  int frequencyCount;

  public void processStartElement2(String namespaceURI, String localName,
                                   String qName, HashMap atts) {
    if (localName.equals("normalCoordinate")) {
      //int atomCount = atomSetCollection.getLastAtomSetAtomCount();
      String wavenumber = "";
      String units = "";
      try {
        atomSetCollection.cloneLastAtomSet();
      } catch (Exception e) {
        e.printStackTrace();
        atomSetCollection.errorMessage = "Error processing normalCoordinate: " + e.getMessage();
        frequencyCount = 0;
        return;
      }
      frequencyCount++;
      if (atts.containsKey("wavenumber")) {
        wavenumber = (String) atts.get("wavenumber");
        if (atts.containsKey("units"))
          units = (String) atts.get("units");

        //never fully implemented

        atomSetCollection.setAtomSetProperty("Frequency", wavenumber + " "
            + units);
        keepChars = true;
      }
      return;
    }

    if (localName.equals("vibrations")) {
      frequencyCount = 0;
      return;
    }
  }

  public void processEndElement2(String uri, String localName, String qName) {
    if (localName.equals("normalCoordinate")) {
      int atomCount = atomSetCollection.getLastAtomSetAtomCount();
      tokens = getTokens(chars);
      Atom[] atoms = atomSetCollection.getAtoms();
      int baseAtomIndex = atomSetCollection.getCurrentAtomSetIndex() * atomCount;
      for (int offset = tokens.length - atomCount * 3, i = 0; i < atomCount; i++) {
        Atom atom = atoms[i + baseAtomIndex];
        atom.vectorX = parseFloat(tokens[offset++]);
        atom.vectorY = parseFloat(tokens[offset++]);
        atom.vectorZ = parseFloat(tokens[offset++]);
      }
    }
  }

  class MolproHandler extends CmlHandler {

    MolproHandler() {
    }

    MolproHandler(XMLReader xmlReader) {
      setHandler(xmlReader, this);
    }

    public void startElement(String namespaceURI, String localName,
                             String qName, Attributes attributes) {
      super.startElement(namespaceURI, localName, qName, attributes);
      processStartElement2(namespaceURI, localName, qName, atts);
    }

    public void endElement(String uri, String localName, String qName) {
      processEndElement2(uri, localName, qName);
      super.endElement(uri, localName, qName);
    }
  }
}
