---
layout: page
title: Genpass
permalink: /genpass/
---

# Generate password

After you have created a sitekey, the password for that site can be generated using:

```bash
> passme site [master]
```

Where:
*   `site`: The site name.
*   `master`: Your master password (optional).

If the master password is not provided as a command-line argument, you will be prompted to enter it securely.

**Security Warning:** If you enter the master password directly in the command line, it may be stored in your shell history file (e.g., `.bash_history`). It is safer to let the program prompt you for it.

### Example

The comment associated with the sitekey is displayed first. After you provide the master password, the generated password is shown and copied to the clipboard.

```text
> passme google
Master password: (input master password)
ID: sekifake
https://google.com/
OT9BD5h6cHmWlN
Password copied to clipboard.
```

Now you can always retrieve your password as long as you have the same sitekey and master password. You can now update the password on the website to match this generated one.

**Important:** Do not mistype your master password when setting your password on a site for the first time. If you do, it will be very difficult to recover that specific "mistyped" version later. 
*   It is recommended to verify your master password by temporarily setting `ShowMasterPass = True` in your [.passme](../config/) file.
*   Alternatively, generate the password several times to confirm that the same password is produced consistently before using it.

### Search by comment

If the provided site name is not found in the sitekey file, the program searches for the keyword within the comments. If matches are found, they are displayed as suggested site names. Therefore, it is recommended to include keywords (like URL or service type) in the comments so that the site name can easily be recalled if you forget it.

---

[Top page](../)