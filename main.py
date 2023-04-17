import asyncio

from asyncua import Server, ua, Node


async def main():
    server = await create_server()

    ns = await setup_namespace(server)

    await create_nodes(ns, server)

    async with server:
        print(f"Listening at {server.endpoint.geturl()}")
        while True:
            await asyncio.sleep(1)


async def create_server():
    server = Server()
    await server.init()

    server.set_endpoint("opc.tcp://0.0.0.0:4840/plc/")
    server.set_server_name("PLC")
    server.set_security_policy([
        ua.SecurityPolicyType.NoSecurity,
    ])

    return server


async def setup_namespace(server) -> int:
    uri = "http://robotic-platform.wp4.big-map.eu"
    ns = await server.register_namespace(uri)
    return ns


async def create_nodes(ns, server: Server):
    lle_object: Node = await server.nodes.objects.add_object(ns, "LLE")

    is_started_variable: Node = await lle_object.add_variable(ns, "IsStarted", False)
    await is_started_variable.set_writable()

    lle_status: Node = await lle_object.add_variable(ns, "Status", "Idle")
    await lle_status.set_writable()


if __name__ == "__main__":
    asyncio.run(main())
