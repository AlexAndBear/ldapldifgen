import click

def generateData(amount):
    data = []
    for i in range(1, amount+1):
        data.append({
            'dn': f"cn=foobar{i},ou=users,dc=example,dc=org",
            'objectClass': ['inetOrgPerson', 'posixAccount', 'shadowAccount'],
            'cn' : f"foobar{i}",
            'gidNumber': '1001',
            'givenName': 'Foo',
            'displayName': f"Foo Bar{i}",
            'sn': f"Bar{2}",
            'uid': f"foobar{i}",
            'uidNumber': str(1000+i),
            'userPassword': f"foobar{i}",
            'homeDirectory': f"/home/foobar{i}"
        })

    return data

def writeToFile(data):
    f = open("generated.ldif", "w")
    f.write("version: 1\n")

    for dataSet in data:
        f.write("\n")
        for index,data in dataSet.items():
            if isinstance(data,list):
                for listItem in data:
                    f.write(f"{index}: {listItem}\n")
            else:
                f.write(f"{index}: {data}\n")

    f.close()


@click.command()
@click.argument('amount')
def main(amount):
    data = generateData(int(amount))
    writeToFile(data)
    click.echo("Done")


if __name__ == '__main__':
    main()