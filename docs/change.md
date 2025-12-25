---
layout: page
title: Change
permalink: /change/
---

# Changing the password

You can overwrite an existing sitekey using the `passme add` command by specifying a site name that already exists. 

**Warning:** You must be careful because once the sitekey is updated, the old password cannot be restored (unless you are using a version control system). Therefore, you will be prompted to type `SURE` to confirm overwriting the sitekey.

### How to change your password

You can change your password for a specific site by following these steps:

1.  **Backup your sitekey file.**
2.  Login to the target site and go to the password change form. Input your old password.
3.  Update the sitekey by running the `passme add` command for the same site name, or by directly [editing](../edit/) the seed section of the sitekey file (e.g., adding some random characters to the seed). Editing the file directly saves you from re-entering comments.
4.  Display the new password using `passme` and input this new password into the site's form.
5.  Keep the backup file until you have successfully changed the password and logged in with the new one.

### Alternative method

Another way to manage a password change is to rename the old site entry in the sitekey file (e.g., change `[google]` to `[google-old]`) and then create a completely new entry for `google`. This ensures the old password remains available via the `google-old` command until you verify the new one works, after which you can delete the old entry.

---

[Top page](../)