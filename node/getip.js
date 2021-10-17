var dns = require('dns');

function hostnameLookup(hostname) {
    dns.lookup(hostname, function(err, addresses, family) {
        console.log(addresses);
    });
}


if (procces.argv.length <= 2) {
    console.log("USAGE: " + __filename + " IPADDR")
    procces.exit(-1)
}

var hostname = procces.argv[2]
console.log('Checking IP of: ${hostname}')
hostnameLookup(hostname);