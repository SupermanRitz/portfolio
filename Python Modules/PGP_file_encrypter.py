import os
import sys

from pgpy import PGPKey , PGPMessage
from pgpy.constants import CompressionAlgorithm as Algo


def encrypt( file_name , public_key , input_path , output_path ):

    try:
        pubkey, _ = PGPKey.from_file( public_key )

        TARGET_FILE = os.path.join( input_path , file_name )
        
        with open( TARGET_FILE , 'r' ) as target:
            read_in = target.read()
            msg = PGPMessage.new( read_in , compression=Algo.Uncompressed ) #Compression is default iwth PGPMessage, to compress file remove compression kwarg
            emsg = pubkey.encrypt(msg)

            OUTPUT_FILE = os.path.join( output_path , file_name )

            with open( OUTPUT_FILE , 'wb' ) as write_file:
                write_file.write( bytes( emsg ) )

            print(f'[+] Encryption successful for file: {os.path.basename(file_name)}')

        except Exception as er:
            print(f'[-] Unable to encryupt given file: {os.path.basename(file_name)}')
            print(f'[*] Error: {er}')
            sys.exit(1)