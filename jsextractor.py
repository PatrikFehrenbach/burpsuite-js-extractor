from burp import IBurpExtender
from burp import IContextMenuFactory
from burp import IContextMenuInvocation

from javax.swing import JMenuItem, JFileChooser
from java.awt import Toolkit
from java.awt.datatransfer import StringSelection
from java.io import FileWriter

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("JS File Extractor with Clipboard Support")
        self._callbacks.registerContextMenuFactory(self)

    def createMenuItems(self, invocation):
        self.context = invocation
        menu_list = []
        menu_list.append(JMenuItem("Extract JS Files to File", actionPerformed=lambda x, inv=invocation: self.extract_js_files(inv)))
        menu_list.append(JMenuItem("Copy JS Files to Clipboard", actionPerformed=lambda x, inv=invocation: self.copy_js_files_to_clipboard(inv)))
        return menu_list

    def extract_js_files(self, invocation):
        fileChooser = JFileChooser()
        returnValue = fileChooser.showSaveDialog(None)
        if returnValue == JFileChooser.APPROVE_OPTION:
            selectedFile = fileChooser.getSelectedFile()
            with open(selectedFile.getPath(), 'w') as file:
                js_files = self.get_js_files(invocation)
                for js_file in js_files:
                    file.write(js_file + '\n')

    def copy_js_files_to_clipboard(self, invocation):
        js_files = self.get_js_files(invocation)
        string_to_copy = '\n'.join(js_files)
        stringSelection = StringSelection(string_to_copy)
        clipboard = Toolkit.getDefaultToolkit().getSystemClipboard()
        clipboard.setContents(stringSelection, None)

    def get_js_files(self, invocation):
        selected_messages = invocation.getSelectedMessages()
        target_domains = set()
        js_files = set()
        if selected_messages:
            for message in selected_messages:
                url = self._helpers.analyzeRequest(message).getUrl()
                target_domains.add(url.getHost())

            sitemap = self._callbacks.getSiteMap(None)
            for item in sitemap:
                request_info = self._helpers.analyzeRequest(item)
                url = request_info.getUrl()
                if url.getHost() in target_domains:
                    response = item.getResponse()
                    if response:
                        response_info = self._helpers.analyzeResponse(response)
                        headers = response_info.getHeaders()
                        if any("javascript" in header for header in headers):
                            js_files.add(str(url))
        return js_files
