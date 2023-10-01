=====================
<==MANAGE CONTACTS==>
=====================

.. contents::

Contacts can be managed throgh an instance of 
:class: contacts.Application , use :meth: contacts.Application.run
to execute any command like ou would in the shell.

ADDING CONTACTS 
===============

.. code-block::
    app.run("contacts add Name 0123456789")

LISTING CONTACTS
================

.. code-block:: 
    app.run("contacts ls")

    