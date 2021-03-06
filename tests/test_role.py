from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_maven_color(Command):
    assert Command("mvn help:help").rc == 0

    # Need to run with bash for ANSI-C Quoting support
    cmd = Command("bash -c %s",
                  "mvn help:help -Dmaven.color=true | grep -Eq $'\e'")
    assert cmd.rc == 0
