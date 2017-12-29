AES keywrap
'''''''''''
implementation of RFC 3394 AES key wrapping/unwrapping

http://www.ietf.org/rfc/rfc3394.txt

also, alternative IV per RFC 5649

http://www.ietf.org/rfc/rfc5649.txt

This is a symmetric key-encryption algorithm.  It should only be used
to encrypt keys (short and globally unique strings.)

In documentation, the key used for this kind of algorithm is
often called the KEK (Key-Encryption-Key), to distinguish
it from data encryption keys.


Why a special key-encryption algorithm?
'''''''''''''''''''''''''''''''''''''''

In a word: size.  By assuming keys are high enough
entropy to be globally unique, and small enough
not to require streaming encryption, aes-keywrap is able to avoid
an IV (initial value) or nonce that increases the size
of the ciphertext.  This can be a significant
savings -- if the data being encrypted is a 32
byte AES-256 key, AES-GCM would result in a
60 byte ciphertext (87% overhead), AES-CTR or AES-CBC would result
in a 48 byte ciphertext (50% overhead) and would also not provide
authenticated encryption, but aes-keywrap
would result in a 32 byte ciphertext (no overhead).

In an application where there are many keys being generated
and encrypted (e.g. a separate data encryption key for
each row in a database), this overhead can be significant.

Another important use case is compatibility with
existing systems.
