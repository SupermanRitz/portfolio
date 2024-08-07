import paramiko

#local_filepath and remote_filepath require full paths
#if you get a "Permission Denied" error check that you have created a remote_filepath that includes the remote 'directory/filename'

def sftp_send_file(hostname, port, username, password, local_filepath, remote_filepath):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        client.connect(hostname, port=port, username=username, password=password)
        
        # Open an SFTP session
        sftp = client.open_sftp()
        
        # Upload the file
        sftp.put(local_filepath, remote_filepath)
        print(f'Successfully uploaded {local_filepath} to {remote_filepath}')
        
        # Close the SFTP session and SSH client
        sftp.close()
        client.close()
        
    except Exception as e:
        print(f'An error occurred: {e}')


        