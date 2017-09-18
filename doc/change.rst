Changing the password
=======================

You can overwrite a sitekey with **passme add** command, if you just specify the site name which already exists. You have to be careful because once the sitekey is updated, the old password cannot be restored (unless you are using version control system). Therefore you will be prompted to type 'SURE' to overwrite the sitekey. You can change your password of a specific site as follows. Actually you can directly `edit <edit.rst>`_ the seed of the sitekey file (just add some characters) to update your password. In this way you do not have to reenter the comment.

* Backup your sitekey file.
* Login to the site and go to password change form. Input the old password.
* Update the sitekey by editing the seed section of the sitekey file with **passme add** command.
* Show the new password with passme and input the new password to the site.
* Keep the backup file until you succeed in changing the password.

Another way is to rename the old site to something like **google-old** by editing the sitekey file and create a new password. This way the old password is available until you delete the old entry.

----

Toppage_

.. _Toppage: README.rst
