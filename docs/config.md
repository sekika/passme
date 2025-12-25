---
layout: page
title: Config
permalink: /config/
---

# Configuration

You can set various configurations in the `.passme` file located in your home directory.

From version 1.1.0 onwards, if a `.passme` file exists in the **current directory**, the configuration is read from there instead of the home directory.

| Variable | Default value | Available values |
| :--- | :--- | :--- |
| SiteKeyFile | (none) | Any filename |
| DefaultHash | sha3_384 | sha384, sha512, sha3_384, sha3_512 (see note) |
| ShowMasterPass | False | True, False |
| ShowPass | True | True, False |
| CopyPass | True | True, False |
| SeedLen | 30 | Integer |
| OpenEditor | (none) | Command (e.g., `vim`, `nano`, `code`) |
| VCS | (none) | git |

### Explanation of variables

*   **SiteKeyFile**: The filename of your sitekey file.
*   **DefaultHash**: The hash algorithm used for new sites. This is stored in the sitekey file for each entry. 
*   **ShowMasterPass**: If set to `True`, the master password you type is shown on the terminal (not masked).
*   **ShowPass**: If set to `True`, the generated password is displayed on the terminal.
*   **CopyPass**: If set to `True`, the generated password is automatically copied to the clipboard. 
    *   *Note:* This feature may not be available if you are using a remote shell (SSH).
*   **SeedLen**: The length of the random seed used for creating passwords.
*   **OpenEditor**: The command to launch a text editor on your system. This is used by the `passme edit` command. See [Edit](../edit/) for details.
*   **VCS**: If set to `git`, changes to the sitekey file are automatically committed to the git repository after running `passme add`. The changes are then reviewed using the `git log -p -1` command.

---

[Top page](../)