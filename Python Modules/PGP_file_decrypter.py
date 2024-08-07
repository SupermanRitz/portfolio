import os
import sys
import warnings
from getpass import getpass

from pgpy import PGPKey , PGPMessage


def decrypt( file_path , private_key , pass_phrase , input_path , output_path ):

    try:
        msg = PGPMessage()
        emsg = msg.from_file( os.path.join( input_path , file_path ) )

        privkey, _ = PGPKey.from_file( private_key )

        with privkey.unlock( pass_phrase ):
            data = privkey.decrypt(emsg)

            if not data.is_encrypted:
                path = os.path.join( output_path , file_path )

                with open( path , 'wt' ) as write_file:
                    write_file.write( str( data.message ) )

                print( f"[+] Decryption successful for file :  {os.path.basename( file_path )}" )
            
            else:
                print( f"[-] Unable to decrypt given file : {os.path.basename(file_path)}" )

    except Exception as e:
        print( f"[-] Unable to decrypt given file : {os.path.basename(file_path)}" )
        print( f"[-] Error : {e} " )
        sys.exit(1)