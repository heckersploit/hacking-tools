#include <iostream>
#include <string>
#include <socket>

using namespace std;

void scan(string targets, int ports) {
    cout << "\n" << "starting scan for" << targets << endl;
    for (int port = 1; port < ports; port++) {
        scan_port(targets, port);
    }
}

void scan_port(string address, int port) {
    try {
        socket sock;
        sock.connect((address, port));
        cout << "port open" << port << endl;
        sock.close();
    }
    catch (...) {
        pass;
    }
}

int main() {
    string targets = input("enter targets to scan(split them by ,)");
    int ports = int(input("enter how many port you want to scan"));

    if (targets.find(",") != string::npos) {
        cout << "scanning multiple targets" << endl;
        for (string ipaddr : targets.split(",")) {
            scan(ipaddr.strip(" ", ports));
        }
    }
    else {
        scan(targets, ports);
    }
    return 0;
}