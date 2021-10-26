from netmiko import ConnectHandler
import subprocess

DEVICE_IP = {
'nn' : '1.1.1.1',
# 'minsk' : '2.2.2.2',
'kazan' : '3.3.3.3',
'rostov' : '4.4.4.4',
'vladimir' : '5.5.5.5',
'volgograd' : '6.6.6.6',
'cheboksary' : '7.7.7.7',
# 'chelyabinsk' : '8.8.8.8',
'omsk' : '9.9.9.9',
'sevastopol' : '10.10.10.10',
'perm' : '11.11.11.11',
'krasnoyarsk' : '12.12.12.12',
'spb' : '13.13.13.13',
'tomsk' : '14.14.14.14',
'belgorod' : '15.15.15.15',
# 'bookkeeping' : '16.16.16.16',
'irkutsk' : '17.17.17.17',
'khabarovsk' : '18.18.18.18',
'barbados' : '19.19.19.19',
'pimsk' : '20.20.20.20',
'cetk' : '21.21.21.21'
}

def copy_config():
    for CITY, IP in DEVICE_IP.items():
        reply = subprocess.run(['ping', '-n', '1', IP])
        if reply.returncode == 0:
            DEVICES_PARAMS = { 
                'device_type' : 'cisco_asa',
                'ip'          : IP,
                'username'    : 'username',
                'password'    : 'password',
                'global_delay_factor' : 2 }
            connect = ConnectHandler(**DEVICES_PARAMS)
            connect.send_command('enable\n\n')
            config = connect.send_command('more system:running-config')

            with open(CITY, 'w') as cfg:
                cfg.writelines(config)
                
            connect.disconnect()

        else:
            continue

if __name__ == '__main__':
    copy_config()
