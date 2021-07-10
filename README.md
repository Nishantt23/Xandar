# Xandar

## What is Xandar ?

Xandar is an email OSINT tool. It finds out a lot of juicy information about the target email address.

#### Features:

* Email Verification { Checks if email exist }
* Checks social media accounts associated w/ the Email 
* Checks data breaches associated w/ the Email
* Find related emails 
* Find related phone numbers
* Find related domains
* Scan Pastebin Dumps for leaked passwords
* Google Search for juicy info related to the Email
* DNS Lookup


## APIs:

| Service | Function | Status |
| :--- | :--- | :--- |
| [verify-email](https://verify-email.org/) | Email Verification | :white\_check\_mark: :key: |
| [hunter.io](https://hunter.io/) - Free Tier | Related Emails | :white\_check\_mark: :key: |
| [leak-lookup](https://leak-lookup.com/) | Breached Sites Names | :white\_check\_mark: :key: |
| [hackertarget](https://hackertarget.com/) | DNS Lookup | :white\_check\_mark: |

:white\_check\_mark: : Service Up and Running!

:key: : API Key required

#### For Use:

Save your API keys in `config.json`

## Cloning:

`git clone https://github.com/Nishantt23/Xandar.git`

## Usage:

`pip3 install -r requirements.txt`

* Edit the `config.json` file adding the API keys

* Set Target Email [ -e / --email ]

`python3 xandar.py -e example@website.com`
