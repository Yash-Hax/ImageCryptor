# Image Encryption Tool

This is a Python tool that can be used to encrypt and decrypt images using the AES encryption algorithm. The tool makes use of the Cryptodome library, which is a self-contained Python package of low-level cryptographic primitives that supports both Python 2.x and 3.x.

## Uses

This tool can be used to securely encrypt and decrypt images with a 256-bit key. It is particularly useful for those who want to protect sensitive images from unauthorized access.

## Prerequisites

To use this tool, you will need Python 3.x and the Cryptodome library installed on your system. You can install Cryptodome using pip with the following command:

``` pip install pycryptodome ```


## Installation

To install this tool, you can clone this repository using the following command:

``` git clone https://github.com/yash-hax/ImageCrypto.git ```


## Usage

To encrypt an image, run the following command:

``` python encrypt_image.py input_file output_file ```


To decrypt an image, run the following command:

``` python decrypt_image.py input_file output_file nonce_file ```


## License

This tool is licensed under the MIT License. See the LICENSE file for more information.


