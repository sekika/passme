---
layout: page
title: Edit
permalink: /edit/
---

# Edit the sitekey file

The [sitekey file](../sitekey/) can be edited with a text editor using the following command:

```bash
> passme edit
```

If this is your first time running this command, you will be prompted to enter the command to open your preferred text editor (e.g., `vim`, `nano`, `notepad`). This setting is stored in the **OpenEditor** variable in your [configuration](../config/).

The system invokes the command as `<OpenEditor> <Name of the sitekey file>`.

This function is useful when you want to view the sitekey file or manually modify it. **Be careful** not to edit lines unintentionally, as changing the seed or parameters will alter your generated passwords.

---

[Top page](../)