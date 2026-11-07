---
layout: page
title: Mobile
permalink: /mobile/
---

# Passme on mobile devices

Passme offers a Flutter-based iOS app and a JavaScript version for web browsers. Neither requires Python on your phone. Keep your sitekey file and its backups on your PC, where you add and edit sites with the Python / CLI version.

## Choose a mobile version

| | iOS app | JavaScript version |
| :--- | :--- | :--- |
| Installation | [App Store](https://apps.apple.com/us/app/password-passme/id6830239169) | Generate an HTML file with `passme html` |
| Sitekey transfer | Import the sitekey file | Selected sites are included in the generated HTML |
| Updates | Import the updated sitekey file again | Regenerate and transfer the HTML |
| `ans95` character set | Supported | Not supported |

The iOS app is available now. An Android app has not been released; the JavaScript version provides a browser-based option for mobile devices. See the [JavaScript guide](../javascript/) for its setup and usage.

## Install and use the iOS app

1. Install [Password Passme from the App Store](https://apps.apple.com/us/app/password-passme/id6830239169).
2. Transfer your PC's plain-text [sitekey file](../sitekey/) to your phone using AirDrop to Files or a cloud provider such as iCloud Drive. Cloud providers may require setup and a network connection.
3. Tap **Import sitekey** and select the file in the system file picker. Choose the sitekey file, not the PC's `.passme` settings or a generated HTML file.
4. Review the validation result and site counts, then confirm. **Every import replaces the entire saved collection.** Sites absent from the new file are removed.
5. Select a site, enter your master password, and tap **Generate**. The result starts masked; tap **Show** or **Copy** to use it. You can tap **Clear** to clear the input and result.

Use the same master password as on your PC to generate the same password. The app cannot detect a mistyped master password: a different master produces a different result.

## Updates and backups

The app stores an independent encrypted copy of the imported sitekeys. Moving or deleting the original transfer file does not affect this copy. Updating the PC file does not update the app automatically.

Site editing and automatic synchronization are not available in the app. After adding a site or changing its settings on your PC, import the updated file again. An import replaces the collection rather than merging it, and there is no history, rollback, or export feature. Keep your authoritative PC file and backups so you can restore the collection by importing it again.

After reinstalling the app, changing phones, or if saved data cannot be read, reimport your sitekey file from your PC.

## Offline use and data protection

After import, normal password generation works offline. The app does not persist the master password or generated passwords. Leaving the app, locking the device, or one minute without interaction clears the master input and result.

The app attempts to clear a copied password after 30 seconds if the clipboard contents have not changed. Background execution and protection from other apps reading the clipboard cannot be guaranteed.

The transfer file remains plain text, including any copy kept in cloud storage. Passme does not delete it. Delete unneeded transfer copies yourself after importing, while retaining the authoritative PC file and secure backups. See [Security](../security/) for storage details and risks shared by all versions.

---

[Top page](../)
