/* $RCSfile$
 * $Author jonathan gutow$
 * $Date Aug 5, 2007 9:19:06 AM $
 * $Revision$
 *
 * Copyright (C) 2005-2007  The Jmol Development Team
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
 *  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
 *  02110-1301, USA.
 */
package org.openscience.jmol.app.webexport;

import java.awt.*;
import java.io.*;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.net.URL;
import java.util.ArrayList;
import java.util.zip.GZIPOutputStream;

import javax.swing.*;

import org.jmol.api.JmolViewer;
import org.jmol.i18n.GT;
import org.jmol.util.ArrayUtil;
import org.jmol.util.Parser;
import org.jmol.util.TextFormat;
import org.jmol.viewer.FileManager;
import org.openscience.jmol.app.HelpDialog;

/*
 * an abstract class used as the basis for the tabbed panels
 * in WebExport. (PopInJmol and ScriptButtons)
 *  
 */
abstract class WebPanel extends JPanel implements ActionListener {

  abstract String getAppletDefs(int i, String html, StringBuffer appletDefs,
                                JmolInstance instance);

  abstract String fixHtml(String html);

  abstract JPanel appletParamPanel(); //should be defined in the code for the specific case e.g. ScriptButtons.java

  protected String panelName; //pop_in or script_button

//  infoFile = "pop_in_instructions";
//  infoFileLocalized = "pop_in_instructions_" + lang + ".html";
//  templateName = "pop_in_template.html";
//  appletTemplateName = "pop_in_template2.html";

  //protected String templateName;
  //protected String infoFile;
  //protected String appletTemplateName;
  //protected String templateImage;
  
  protected String htmlAppletTemplate;
  protected String listLabel;
  protected String appletInfoDivs;
  protected boolean useAppletJS;

  protected JSpinner appletSizeSpinnerW;
  protected JSpinner appletSizeSpinnerH;
  protected JSpinner appletSizeSpinnerP;

  private JScrollPane editorScrollPane;
  private JButton saveButton, helpButton, addInstanceButton;
  private JButton deleteInstanceButton, showInstanceButton;
  private JTextField remoteAppletPath, localAppletPath, pageAuthorName, webPageTitle;
  private JFileChooser fc;
  private JList instanceList;
  private JmolViewer viewer;
  private int panelIndex;
  private WebPanel[] webPanels;

  protected WebPanel(JmolViewer viewer, JFileChooser fc, WebPanel[] webPanels,
      int panelIndex) {
    this.viewer = viewer;
    this.fc = fc;
    this.webPanels = webPanels;
    this.panelIndex = panelIndex;
    //Create the text fields for the path to the Jmol applet, page author(s) name(s) and  web page title.
    remoteAppletPath = new JTextField(20);
    remoteAppletPath.addActionListener(this);
    remoteAppletPath.setText(WebExport.getAppletPath(true));
    localAppletPath = new JTextField(20);
    localAppletPath.addActionListener(this);
    localAppletPath.setText(WebExport.getAppletPath(false));
    pageAuthorName= new JTextField(20);
    pageAuthorName.addActionListener(this);
    pageAuthorName.setText(WebExport.getPageAuthorName());
    webPageTitle = new JTextField(20);
    webPageTitle.addActionListener(this);
    webPageTitle.setText(GT._("A web page containing Jmol applets"));
  }

  //Need the panel maker and the action listener.

  JPanel getPanel(int infoWidth, int infoHeight) {

    //For layout purposes, put things in separate panels
   
    //Create the list and list view to handle the list of 
    //Jmol Instances.
    instanceList = new JList(new DefaultListModel());
    instanceList.setSelectionMode(ListSelectionModel.SINGLE_INTERVAL_SELECTION);
    instanceList.setTransferHandler(new ArrayListTransferHandler(this));
    instanceList.setCellRenderer(new InstanceCellRenderer());
    instanceList.setDragEnabled(true);
    instanceList.setPreferredSize(new Dimension(350, 200));

    JScrollPane instanceListView = new JScrollPane(instanceList);
    instanceListView.setPreferredSize(new Dimension(350, 200));
    JPanel instanceSet = new JPanel();
    instanceSet.setLayout(new BorderLayout());
    instanceSet.add(new JLabel(listLabel), BorderLayout.NORTH);
    instanceSet.add(instanceListView, BorderLayout.CENTER);
    instanceSet.add(new JLabel(GT._("double-click and drag to reorder")),
        BorderLayout.SOUTH);

    //Create the Instance add button.
    addInstanceButton = new JButton(GT._("Add Present Jmol State as Instance..."));
    addInstanceButton.addActionListener(this);

    JPanel buttonPanel = new JPanel();
    buttonPanel.setMaximumSize(new Dimension(350, 50));
    showInstanceButton = new JButton(GT._("Show Selected"));
    showInstanceButton.addActionListener(this);
    deleteInstanceButton = new JButton(GT._("Delete Selected"));
    deleteInstanceButton.addActionListener(this);
    buttonPanel.add(showInstanceButton);
    buttonPanel.add(deleteInstanceButton);

    // width height or %width

    JPanel paramPanel = appletParamPanel();
    paramPanel.setMaximumSize(new Dimension(350, 70));

    //Instance selection
    JPanel instanceButtonPanel = new JPanel();
    instanceButtonPanel.add(addInstanceButton);
    instanceButtonPanel.setSize(300, 70);

    JPanel p = new JPanel();
    p.setLayout(new BorderLayout());
    p.add(instanceButtonPanel, BorderLayout.NORTH);
    p.add(buttonPanel, BorderLayout.SOUTH);

    JPanel instancePanel = new JPanel();
    instancePanel.setLayout(new BorderLayout());
    instancePanel.add(instanceSet, BorderLayout.CENTER);
    instancePanel.add(p, BorderLayout.SOUTH);

    JPanel rightPanel = new JPanel();
    rightPanel.setLayout(new BorderLayout());
    rightPanel.setMinimumSize(new Dimension(350, 350));
    rightPanel.setMaximumSize(new Dimension(350, 1000));
    rightPanel.add(paramPanel, BorderLayout.NORTH);
    rightPanel.add(instancePanel, BorderLayout.CENTER);
    rightPanel.setBorder(BorderFactory.createTitledBorder(GT._("Jmol Instances:")));

    //Create the overall panel
    JPanel panel = new JPanel();
    panel.setLayout(new BorderLayout());

    JPanel leftPanel = getLeftPanel(infoWidth, infoHeight);
    leftPanel.setMaximumSize(new Dimension(350, 1000));

  
    //Add everything to this panel.
    panel.add(leftPanel, BorderLayout.CENTER);
    panel.add(rightPanel, BorderLayout.EAST);

    enableButtons(instanceList);
    return panel;
  }

  private JPanel getLeftPanel(int w, int h) {

    helpButton = new JButton(GT._("Help/Instructions"));
    helpButton.addActionListener(this);

    String templateImage = panelName + ".png";
    URL pageCartoon = WebExport.getResource(this, templateImage);
    ImageIcon pageImage = null;
    if (pageCartoon != null) {
      pageImage = new ImageIcon(pageCartoon, GT._("Cartoon of Page"));
    } else {
      System.err.println("Error Loading Page Cartoon Image " + templateImage);
    }
    JLabel pageCartoonLabel = new JLabel(pageImage);
    JPanel pageCartoonPanel = new JPanel();
    pageCartoonPanel.setLayout(new BorderLayout());
    pageCartoonPanel.setBorder(BorderFactory.createTitledBorder(GT
        ._("Cartoon of Page")+":"));
    pageCartoonPanel.add(pageCartoonLabel);
    //   editorScrollPane = getInstructionPane(w, h);

    //Create the save button. 
    saveButton = new JButton(GT._("Save HTML as..."));
    saveButton.addActionListener(this);
    JPanel savePanel = new JPanel();
    savePanel.add(saveButton);

    //Path to applet panel

    JPanel pathPanel = new JPanel();
    pathPanel.setLayout(new BorderLayout());
    pathPanel.setBorder(BorderFactory.createTitledBorder(GT
        ._("Relative server path to jar files:")));
    pathPanel.add(remoteAppletPath, BorderLayout.NORTH);

    JPanel pathPanel2 = new JPanel();
    pathPanel2.setLayout(new BorderLayout());
    pathPanel2.setBorder(BorderFactory.createTitledBorder(GT
        ._("Relative local path to jar files:")));
    pathPanel2.add(localAppletPath, BorderLayout.NORTH);

    //Page Author Panel
    JPanel authorPanel = new JPanel();
    authorPanel.setBorder(BorderFactory.createTitledBorder(GT
        ._("Author (your name):")));
    authorPanel.add(pageAuthorName, BorderLayout.NORTH);

    //Page Title Panel
    JPanel titlePanel = new JPanel();
    titlePanel.setLayout(new BorderLayout());
    titlePanel.setBorder(BorderFactory.createTitledBorder(GT
        ._("Browser window title for this web page:")));
    titlePanel.add(webPageTitle, BorderLayout.NORTH);
    titlePanel.add(savePanel, BorderLayout.SOUTH);

    JPanel pathPanels = new JPanel();
    pathPanels.setLayout(new BorderLayout());
    pathPanels.add(pathPanel, BorderLayout.NORTH);
    pathPanels.add(pathPanel2, BorderLayout.SOUTH);
    JPanel settingsPanel = new JPanel();
    settingsPanel.setLayout(new BorderLayout());
    settingsPanel.add(pathPanels, BorderLayout.NORTH);
    settingsPanel.add(authorPanel, BorderLayout.CENTER);
    settingsPanel.add(titlePanel, BorderLayout.SOUTH);

    //Combine previous three panels into one
    JPanel leftpanel = new JPanel();
    leftpanel.setLayout(new BorderLayout());
    //   leftpanel.add(editorScrollPane, BorderLayout.CENTER);
    leftpanel.add(helpButton, BorderLayout.NORTH);
    leftpanel.add(pageCartoonPanel, BorderLayout.CENTER);
    leftpanel.add(settingsPanel, BorderLayout.SOUTH);
    return leftpanel;
  }

  int getInfoWidth() {
    return editorScrollPane.getWidth();
  }

  int getInfoHeight() {
    return editorScrollPane.getHeight();
  }

  public void actionPerformed(ActionEvent e) {

    if (e.getSource() == remoteAppletPath) {//apparently no events are fired to reach this, maybe "enter" does it
      String path = remoteAppletPath.getText();
      WebExport.setAppletPath(path, true);
      return;
    }

    if (e.getSource() == localAppletPath) {//apparently no events are fired to reach this, maybe "enter" does it
      String path = localAppletPath.getText();
      WebExport.setAppletPath(path, false);
      return;
    }

    //Handle open button action.
    if (e.getSource() == addInstanceButton) {
      //make dialog to get name for instance
      //create an instance with this name.  Each instance is just a container for a string with the Jmol state
      //which contains the full information on the file that is loaded and manipulations done.
      String label = (instanceList.getSelectedIndices().length != 1 ? ""
          : getInstanceName(-1));
      String name = JOptionPane.showInputDialog(
          GT._("Give the occurrence of Jmol a name:"), label);
      if (name == null)
        return;
      //need to get the script...
      String script = viewer.getStateInfo();
      if (script == null) {
        LogPanel.log("Error trying to get Jmol State within pop_in_Jmol.");
      }
      DefaultListModel listModel = (DefaultListModel) instanceList.getModel();
      int width = 300;
      int height = 300;
      if (appletSizeSpinnerH != null) {
        width = ((SpinnerNumberModel) (appletSizeSpinnerW.getModel()))
            .getNumber().intValue();
        height = ((SpinnerNumberModel) (appletSizeSpinnerH.getModel()))
            .getNumber().intValue();
      }
      JmolInstance instance = new JmolInstance(viewer, name, script, width, height);
      if (instance == null) {
        LogPanel
            .log(GT._("Error creating new instance containing script(s) and image."));
      }

      int i;
      for (i = instanceList.getModel().getSize(); --i >= 0;)
        if (getInstanceName(i).equals(instance.name))
          break;
      if (i < 0) {
        i = listModel.getSize();
        listModel.addElement(instance);
        LogPanel.log(GT._("added Instance {0}", instance.name));
      } else {
        listModel.setElementAt(instance, i);
        LogPanel.log(GT._("updated Instance {0}", instance.name));
      }
      instanceList.setSelectedIndex(i);
      syncLists();
      return;
    }

    if (e.getSource() == deleteInstanceButton) {
      DefaultListModel listModel = (DefaultListModel) instanceList.getModel();
      //find out which are selected and remove them.
      int[] todelete = instanceList.getSelectedIndices();
      int nDeleted = 0;
      for (int i = 0; i < todelete.length; i++){
        JmolInstance instance = (JmolInstance) listModel.get(todelete[i]);
        try {
          instance.delete();
        } catch (IOException err) {
          LogPanel.log(err.getMessage());
        }
        listModel.remove(todelete[i] - nDeleted++);
      }
      syncLists();
      return;
    }

    if (e.getSource() == showInstanceButton) {
      DefaultListModel listModel = (DefaultListModel) instanceList.getModel();
      //find out which are selected and remove them.
      int[] list = instanceList.getSelectedIndices();
      if (list.length != 1)
        return;
      JmolInstance instance = (JmolInstance) listModel.get(list[0]);
      viewer.evalStringQuiet(")" + instance.script); //leading paren disabled history
      return;
    }

    if (e.getSource() == saveButton) {
      fc.setDialogTitle(GT._("Select a directory to create or an HTML file to save"));
      int returnVal = fc.showSaveDialog(this);
      if (returnVal != JFileChooser.APPROVE_OPTION)
        return;
      File file = fc.getSelectedFile();
      boolean retVal = true;
      try {
        String path = remoteAppletPath.getText();
        WebExport.setAppletPath(path, true);
        path = localAppletPath.getText();
        WebExport.setAppletPath(path, false);
        String authorName = pageAuthorName.getText();
        WebExport.setWebPageAuthor(authorName);
        retVal = fileWriter(file, instanceList);
      } catch (IOException IOe) {
        LogPanel.log(IOe.getMessage());
      }
      if (!retVal) {
        LogPanel.log(GT._("Call to FileWriter unsuccessful."));
      }
    }
    if (e.getSource() == helpButton){
      HelpDialog webExportHelp = new HelpDialog(WebExport.getFrame(), 
          WebExport.getHtmlResource(this, panelName + "_instructions"));
      webExportHelp.setVisible(true);
      webExportHelp.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
    }
  }

  String getInstanceName(int i) {
    if (i < 0)
      i = instanceList.getSelectedIndex();
    JmolInstance instance = (JmolInstance) instanceList.getModel()
        .getElementAt(i);
    return (instance == null ? "" : instance.name);
  }

  boolean fileWriter(File file, JList InstanceList) throws IOException { //returns true if successful.
    useAppletJS = JmolViewer.checkOption(viewer, "webMakerCreateJS");
    //          JOptionPane.showMessageDialog(null, "Creating directory for data...");
    String datadirPath = file.getPath();
    String datadirName = file.getName();
    String fileName = null;
    if (datadirName.indexOf(".htm") > 0) {
      fileName = datadirName;
      datadirPath = file.getParent();
      file = new File(datadirPath);
      datadirName = file.getName();
    } else {
      fileName = datadirName + ".html";
    }
    datadirPath = datadirPath.replace('\\', '/');
    boolean made_datadir = (file.exists() && file.isDirectory() || file.mkdir());
    DefaultListModel listModel = (DefaultListModel) InstanceList.getModel();
    LogPanel.log("");
    if (made_datadir) {
      LogPanel.log(GT._("Using directory {0}", datadirPath));
      LogPanel.log("  " + GT._("adding JmolPopIn.js"));
 
      viewer.writeTextFile(datadirPath + "/JmolPopIn.js",
          WebExport.getResourceString(this, "JmolPopIn.js"));
      for (int i = 0; i < listModel.getSize(); i++) {
        JmolInstance thisInstance = (JmolInstance) (listModel.getElementAt(i));
        String javaname = thisInstance.javaname;
        String script = thisInstance.script;
        LogPanel.log("  ...jmolApplet" + i);
        LogPanel.log("      ..." + GT._("adding {0}.png", javaname));
        try {
          thisInstance.movepict(datadirPath);
        } catch (IOException IOe) {
          throw IOe;
        }

        String fileList = "";
        fileList += addFileList(script, "/*file*/");
        fileList += addFileList(script, "FILE0=");
        fileList += addFileList(script, "FILE1=");
        if (localAppletPath.getText().equals(".")
            || remoteAppletPath.getText().equals("."))
          fileList += "Jmol.js\nJmolApplet.jar";
        String[] filesToCopy = fileList.split("\n");
        String[] copiedFileNames = new String[filesToCopy.length];
        String f;
        int pt;
        for (int iFile = 0; iFile < filesToCopy.length; iFile++) {
          if ((pt = (f = filesToCopy[iFile]).indexOf("|")) >= 0)
            filesToCopy[iFile] = f.substring(0, pt);
          copiedFileNames[iFile] = copyBinaryFile(filesToCopy[iFile],
              datadirPath);
        }
        script = localizeFileReferences(script, filesToCopy, copiedFileNames);
        LogPanel.log("      ..." + GT._("adding {0}.spt", javaname));
        viewer.writeTextFile(datadirPath + "/" + javaname + ".spt", script);
      }
      String html = WebExport.getResourceString(this, panelName + "_template");
      html = fixHtml(html);
      appletInfoDivs = "";
      StringBuffer appletDefs = new StringBuffer();
      if (!useAppletJS)
        htmlAppletTemplate = WebExport.getResourceString(this, panelName + "_template2");
      for (int i = 0; i < listModel.getSize(); i++)
        html = getAppletDefs(i, html, appletDefs, (JmolInstance) listModel
            .getElementAt(i));
      html = TextFormat.simpleReplace(html, "@AUTHOR@", GT.escapeHTML(pageAuthorName
          .getText()));
      html = TextFormat.simpleReplace(html, "@TITLE@", GT.escapeHTML(webPageTitle.getText()));
      html = TextFormat.simpleReplace(html, "@REMOTEAPPLETPATH@",
          remoteAppletPath.getText());
      html = TextFormat.simpleReplace(html, "@LOCALAPPLETPATH@",
          localAppletPath.getText());
      html = TextFormat.simpleReplace(html, "@DATADIRNAME@", datadirName);
      if (appletInfoDivs.length() > 0)
        appletInfoDivs = "\n<div style='display:none'>\n" + appletInfoDivs
            + "\n</div>\n";
      String str = appletDefs.toString();
      if (useAppletJS)
        str = "<script type='text/javascript'>\n" + str + "\n</script>";
      html = TextFormat.simpleReplace(html, "@APPLETINFO@", appletInfoDivs);
      html = TextFormat.simpleReplace(html, "@APPLETDEFS@", str);
      html = TextFormat.simpleReplace(html, "@CREATIONDATA@", GT.escapeHTML(WebExport
          .TimeStamp_WebLink()));
      html = TextFormat.simpleReplace(html, "@AUTHORDATA@",
          GT.escapeHTML(GT._("Based on template by A. Herr&#x00E1;ez as modified by J. Gutow")));
      html = TextFormat.simpleReplace(html, "@LOGDATA@", "<pre>\n"
          + LogPanel.getText() + "\n</pre>\n");
      LogPanel.log("      ..." + GT._("creating {0}", fileName));
      viewer.writeTextFile(datadirPath + "/" + fileName, html);
    } else {
      IOException IOe = new IOException("Error creating directory: "
          + datadirPath);
      throw IOe;
    }
    LogPanel.log("");
    return true;
  }

  private static String addFileList(String script, String tag) {
    String fileList = "";
    int i = -1;
    while ((i = script.indexOf(tag, i + 1)) >= 0) {
      fileList += Parser.getNextQuotedString(script, i) + "\n";
    }
    return fileList;
  }
  
  private static String copyBinaryFile(String fullPathName, String dataPath) {
    String name = fullPathName.substring(fullPathName.lastIndexOf('/') + 1);
    name = dataPath + "/" + name;
    String gzname = name + ".gz";
    File outFile = new File(name);
    File gzoutFile = new File(gzname);
    if (outFile.exists())
      return name;
    if (gzoutFile.exists())
      return gzname;
    try {
      LogPanel.log("      ..." + GT._("copying\n{0}\n         to",fullPathName));
      byte[] data = getFileAsBytes(fullPathName);
      if (data == null)
        LogPanel.log(GT._("Could not find or open:\n{0}", fullPathName));
      else { 
        name = writeFileBytes(name, data); 
        LogPanel.log(name);
      }
    } catch (Exception e) {
      LogPanel.log(e.getMessage());
    }
    return name;
  }
  
  private static byte[] getFileAsBytes(String path) throws IOException {
    int len = 0;
    int totalLen = 0;
    Object streamOrError = FileManager.getInputStream(path, false, null, null);
    if (streamOrError instanceof String) {
      LogPanel.log((String) streamOrError);
      return null;
    }
    byte[] buf = new byte[1024];
    byte[] bytes = new byte[4096];
    BufferedInputStream bis = new BufferedInputStream((InputStream) streamOrError);
    while ((len = bis.read(buf)) > 0) {
      totalLen += len;
      if (totalLen >= bytes.length)
        bytes = ArrayUtil.ensureLength(bytes, totalLen * 2);
      System.arraycopy(buf, 0, bytes, totalLen - len, len);
    }
    bis.close();
    buf = new byte[totalLen];
    System.arraycopy(bytes, 0, buf, 0, totalLen);
    return buf;
  }
  
  private static String writeFileBytes(String path, byte[] data) {
    try {
      if (data.length>=524288 && !path.endsWith("JmolApplet.jar") ){ //gzip it
        path += ".gz";
        GZIPOutputStream gzFile = new GZIPOutputStream(new FileOutputStream(path));
        gzFile.write(data);
        LogPanel.log("      ..." + GT._("compressing large data file to") + "\n");
        gzFile.flush();
        gzFile.close();
      } else {
        FileOutputStream os = new FileOutputStream(path);
        os.write(data);
        os.flush();
        os.close();
      }
    } catch (IOException e) {
      LogPanel.log(e.getMessage());
    }
    return path;
  }
  
  private static String localizeFileReferences(String script, String[] origFileList, String [] copiedFileNames) {
    for (int i = 0; i < origFileList.length; i++) {
      String fullPathName = origFileList[i];
      String fullCopiedName = copiedFileNames[i];
      String name = fullCopiedName.substring(fullCopiedName.lastIndexOf('/') + 1);
      if (!name.equals(fullPathName))
        script = TextFormat.simpleReplace(script, fullPathName,name);
    }
    return script;
  }
  
  
  void syncLists() {
    JList list = webPanels[1 - panelIndex].instanceList;
    DefaultListModel model1 = (DefaultListModel) instanceList.getModel();
    DefaultListModel model2 = (DefaultListModel) list.getModel();
    model2.clear();
    int n = model1.getSize();
    for (int i = 0; i < n; i++)
      model2.addElement(model1.get(i));
    list.setSelectedIndices(new int[] {});
    enableButtons(instanceList);
    webPanels[1 - panelIndex].enableButtons(list);
  }

  void enableButtons(JList list) {
    int nSelected = list.getSelectedIndices().length;
    int nListed = list.getModel().getSize();
    saveButton.setEnabled(nListed > 0);
    deleteInstanceButton.setEnabled(nSelected > 0);
    showInstanceButton.setEnabled(nSelected == 1);
  }

  class InstanceCellRenderer extends JLabel implements ListCellRenderer {

    public Component getListCellRendererComponent(JList list, Object value,
                                                  int index,
                                                  boolean isSelected,
                                                  boolean cellHasFocus) {
      setText(" " + ((JmolInstance) value).name);
      if (isSelected) {
        setBackground(list.getSelectionBackground());
        setForeground(list.getSelectionForeground());
      } else {
        setBackground(list.getBackground());
        setForeground(list.getForeground());
      }
      setEnabled(list.isEnabled());
      setFont(list.getFont());
      setOpaque(true);
      enableButtons(list);
      return this;
    }
  }

}

class ArrayListTransferHandler extends TransferHandler {
  DataFlavor localArrayListFlavor, serialArrayListFlavor;
  String localArrayListType = DataFlavor.javaJVMLocalObjectMimeType
      + ";class=java.util.ArrayList";
  JList source = null;
  int[] sourceIndices = null;
  int addIndex = -1; //Location where items were added
  int addCount = 0; //Number of items added
  WebPanel webPanel;

  ArrayListTransferHandler(WebPanel webPanel) {
    this.webPanel = webPanel;
    try {
      localArrayListFlavor = new DataFlavor(localArrayListType);
    } catch (ClassNotFoundException e) {
      System.out
          .println("ArrayListTransferHandler: unable to create data flavor");
    }
    serialArrayListFlavor = new DataFlavor(ArrayList.class, "ArrayList");
  }

  public boolean importData(JComponent c, Transferable t) {
    if (sourceIndices == null || !canImport(c, t.getTransferDataFlavors())) {
      return false;
    }
    JList target = null;
    ArrayList alist = null;
    try {
      target = (JList) c;
      if (hasLocalArrayListFlavor(t.getTransferDataFlavors())) {
        alist = (ArrayList) t.getTransferData(localArrayListFlavor);
      } else if (hasSerialArrayListFlavor(t.getTransferDataFlavors())) {
        alist = (ArrayList) t.getTransferData(serialArrayListFlavor);
      } else {
        return false;
      }
    } catch (UnsupportedFlavorException ufe) {
      System.out.println("importData: unsupported data flavor");
      return false;
    } catch (IOException ioe) {
      System.out.println("importData: I/O exception");
      return false;
    }

    //At this point we use the same code to retrieve the data
    //locally or serially.

    //We'll drop at the current selected index.
    int targetIndex = target.getSelectedIndex();

    //Prevent the user from dropping data back on itself.
    //For example, if the user is moving items #4,#5,#6 and #7 and
    //attempts to insert the items after item #5, this would
    //be problematic when removing the original items.
    //This is interpreted as dropping the same data on itself
    //and has no effect.
    if (source.equals(target)) {
      //System.out.print("checking indices index TO: " + targetIndex + " FROM:");
      //for (int i = 0; i < sourceIndices.length;i++)
      //System.out.print(" "+sourceIndices[i]);
      //System.out.println("");
      if (targetIndex >= sourceIndices[0]
          && targetIndex <= sourceIndices[sourceIndices.length - 1]) {
        //System.out.println("setting indices null : " + targetIndex + " " + sourceIndices[0] + " " + sourceIndices[sourceIndices.length - 1]);
        sourceIndices = null;
        return true;
      }
    }

    DefaultListModel listModel = (DefaultListModel) target.getModel();
    int max = listModel.getSize();
    if (targetIndex < 0) {
      targetIndex = max;
    } else {
      if (sourceIndices[0] < targetIndex)
        targetIndex++;
      if (targetIndex > max) {
        targetIndex = max;
      }
    }
    addIndex = targetIndex;
    addCount = alist.size();
    for (int i = 0; i < alist.size(); i++) {
      listModel.add(targetIndex++, objectOf(listModel, alist.get(i)));
    }
    return true;
  }

  private static Object objectOf(DefaultListModel listModel, Object objectName) {
    if (objectName instanceof String) {
      String name = (String) objectName;
      Object o;
      for (int i = listModel.size(); --i >= 0;)
        if (!((o = listModel.get(i)) instanceof String)
            && o.toString().equals(name))
          return listModel.get(i);
    }
    return objectName;
  }

  protected void exportDone(JComponent c, Transferable data, int action) {
    //System.out.println("action="+action + " " + addCount + " " + sourceIndices);
    if ((action == MOVE) && (sourceIndices != null)) {
      DefaultListModel model = (DefaultListModel) source.getModel();

      //If we are moving items around in the same list, we
      //need to adjust the indices accordingly since those
      //after the insertion point have moved.
      if (addCount > 0) {
        for (int i = 0; i < sourceIndices.length; i++) {
          if (sourceIndices[i] > addIndex) {
            sourceIndices[i] += addCount;
          }
        }
      }
      for (int i = sourceIndices.length - 1; i >= 0; i--)
        model.remove(sourceIndices[i]);
      ((JList) c).setSelectedIndices(new int[] {});
      if (webPanel != null)
        webPanel.syncLists();
    }
    sourceIndices = null;
    addIndex = -1;
    addCount = 0;
  }

  private boolean hasLocalArrayListFlavor(DataFlavor[] flavors) {
    if (localArrayListFlavor == null) {
      return false;
    }

    for (int i = 0; i < flavors.length; i++) {
      if (flavors[i].equals(localArrayListFlavor)) {
        return true;
      }
    }
    return false;
  }

  private boolean hasSerialArrayListFlavor(DataFlavor[] flavors) {
    if (serialArrayListFlavor == null) {
      return false;
    }

    for (int i = 0; i < flavors.length; i++) {
      if (flavors[i].equals(serialArrayListFlavor)) {
        return true;
      }
    }
    return false;
  }

  public boolean canImport(JComponent c, DataFlavor[] flavors) {
    if (hasLocalArrayListFlavor(flavors)) {
      return true;
    }
    if (hasSerialArrayListFlavor(flavors)) {
      return true;
    }
    return false;
  }

  protected Transferable createTransferable(JComponent c) {
    if (c instanceof JList) {
      source = (JList) c;
      sourceIndices = source.getSelectedIndices();
      Object[] values = source.getSelectedValues();
      if (values == null || values.length == 0) {
        return null;
      }
      ArrayList alist = new ArrayList(values.length);
      for (int i = 0; i < values.length; i++) {
        Object o = values[i];
        String str = o.toString();
        if (str == null)
          str = "";
        alist.add(str);
      }
      return new ArrayListTransferable(alist);
    }
    return null;
  }

  public int getSourceActions(JComponent c) {
    return COPY_OR_MOVE;
  }

  class ArrayListTransferable implements Transferable {
    ArrayList data;

    ArrayListTransferable(ArrayList alist) {
      data = alist;
    }

    public Object getTransferData(DataFlavor flavor)
        throws UnsupportedFlavorException {
      if (!isDataFlavorSupported(flavor)) {
        throw new UnsupportedFlavorException(flavor);
      }
      return data;
    }

    public DataFlavor[] getTransferDataFlavors() {
      return new DataFlavor[] { localArrayListFlavor, serialArrayListFlavor };
    }

    public boolean isDataFlavorSupported(DataFlavor flavor) {
      if (localArrayListFlavor.equals(flavor)) {
        return true;
      }
      if (serialArrayListFlavor.equals(flavor)) {
        return true;
      }
      return false;
    }
  }
}
