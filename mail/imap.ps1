# Get the DLL at UiPath Package manager/

# Load the IMAPX DLL assembly
$dll = 'C:\Users\USER\.nuget\packages\imapx\2.0.0.18\lib\net46\imapx.dll'
[Reflection.Assembly]::LoadFile($dll)

# Setup password for Gmail; because you saved it as a secure string, it can only be decrypted by you.
# However this type of encryption is not 100% impenetrable, so use caution
$pwdgmail = gc ./passgmail.txt | convertto-securestring
$bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pwdgmail)
$Username = "meister.maestro.b.c@gmail.com"
$Password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)

# Initialize the IMAP client
$client = New-Object ImapX.ImapClient

###set the fetching mode to retrieve the part of message you want to retrieve, 
###the less the better
$client.Behavior.MessageFetchMode = "Full"
$client.Host = "imap.gmail.com"
$client.Port = 993
$client.UseSsl = $true
$client.Connect()
$client.Login($Username, $Password)

# Get folder/label object containing emails you want to read from
$res = $client.folders.subfolders | where { $_.path -eq 'path/to/label' }

# Search email threads inside the subfolder
$numberOfMessagesLimit = 10
$messages = $res.search("ALL", $client.Behavior.MessageFetchMode, $numberOfMessagesLimit)

# Display the messages in a formatted table
$messages | ft *