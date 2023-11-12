# Burp Suite JavaScript File Extractor

This Burp Suite extension allows users to extract JavaScript file URLs from the sitemap of a targeted website. It offers the flexibility to select specific items from the sitemap and provides options to save the URLs to a file or copy them to the clipboard.



https://github.com/PatrikFehrenbach/burpsuite-js-extractor/assets/9072595/0dfc85a9-584b-436b-b401-c90dd6bde803




## Installation

1. **Download Jython**:
   - Download the latest standalone Jython jar from the [Jython website](http://www.jython.org/downloads.html).

2. **Configure Jython in Burp Suite**:
   - Open Burp Suite.
   - Go to the `Extender` tab.
   - In the `Options` sub-tab, locate the `Python Environment` section.
   - Click `Select file` and navigate to the Jython jar file you downloaded.

3. **Load the Extension**:
   - Still in the `Extender` tab, switch to the `Extensions` sub-tab.
   - Click the `Add` button.
   - In the dialog, select `Extension Type` as `Python`.
   - Click `Select file` and navigate to the `.py` file of the extension.
   - Click `Next` or `Finish` to load the extension.

## Usage

1. **Select Target Items in Sitemap**:
   - Navigate to the `Target` tab.
   - In the site map, select one or more items from the domain(s) you wish to extract JavaScript files from.

2. **Extract JavaScript Files**:
   - Right-click on the selected item(s).
   - Choose the appropriate option from the context menu:
     - `Extract JS Files to File`: This option allows you to save the JavaScript URLs to a file. Choose the desired location to save the file when prompted.
     - `Copy JS Files to Clipboard`: This option copies all JavaScript URLs to the clipboard, allowing you to paste them elsewhere.

## Notes

- The extension identifies JavaScript files based on the `Content-Type` header in the HTTP response, looking for types that include "javascript".
- Ensure that Burp Suite's spider has adequately crawled the target website to populate the sitemap with relevant JavaScript files.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
