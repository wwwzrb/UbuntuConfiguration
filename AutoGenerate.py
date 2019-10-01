# -*- coding: utf-8 -*-
import json
import glob
import os
from string import punctuation, digits
import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

jsons_dir = "ShadowSocksR"

class Generate:

    def get_json(self):
        jdir = unicode('./gui-config.json')
        with open(jdir, 'r') as f:
            jsn = json.load(f)

        jsons = []
        configs = jsn["configs"]
        for config in configs:
            obj = {}
            obj["remarks"]=config["remarks"]
            obj["server"]=config["server"]
            obj["server_ipv6"]="::"
            obj["server_port"]=config["server_port"]
            obj["local_address"]="127.0.0.1"
            obj["local_port"]=1080

            obj["password"]=config["password"]
            obj["method"]=config["method"]
            obj["protocol"]=config["protocol"]
            obj["protocol_param"]=config["protocolparam"]
            obj["obfs"]=config["obfs"]
            obj["obfs_param"]=config["obfsparam"]
            obj["speed_limit_per_con"]=0
            obj["speed_limit_per_user"]=0

            obj["additional_ports"]= {}
            obj["additional_ports_only"]= False
            obj["timeout"]=120
            obj["udp_timeout"]=60
            obj["dns_ipv6"]= False
            obj["connect_verbose_info"]=0
            obj["redirect"]=""
            obj["fast_open"]=False

            jsons.append(obj)

        return jsons

    def write_json(self, addr):
        jsons = []
        try:
            jsons = self.get_json()
        except Exception as exp:
            var="get_json() Error in class generate:\r\n"+str(exp)
            self.info(var)

        for idx, jsn in enumerate(jsons):
            #print jsn
            try:
                filename = jsn["remarks"]
                filename = filename.decode('utf-8')
                ignoreDict = {ord(c): None for c in (punctuation + ' ' + '\n')}
                filename = filename.translate(ignoreDict)
                print 'writing json file: ', filename
                jsn = json.dumps(jsn)
                with open(os.path.join(addr, filename + '.json'), "w") as f:
                    f.write(jsn)

            except Exception as exp:
                var = "writeJSON() Error in class generate:\r\n" + str(exp)
                self.info(var)

    def info(self, s):
        print s

if __name__ == '__main__':
    generate=Generate()
    generate.write_json(jsons_dir)
