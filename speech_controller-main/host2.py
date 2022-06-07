import asyncio
import websockets

HOST  = '0.0.0.0'
WS_PORT = 3333
TCP_PORT = 8888

loop = asyncio.get_event_loop()

websocket_connections = []
tcp_connections = []


async def send_status(status: str):
	data = status.encode()
	for c in tcp_connections:
		try:
			writer = c[1]
			writer.write(data)
			await writer.drain()
		except Exception as e:
			print(e)

async def executor(command: str):
	command = command.lower()
	words = command.split(" ")
	print(words)
	if 'вправо' in words:
		await send_status('d')
	if 'право' in words:
		await send_status('d')
	if 'права' in words:
			await send_status('d')
	if 'cправа' in words:
			await send_status('d')

	if 'влево' in words:
		await send_status('a')
	if 'лево' in words:
		await send_status('a')
	if 'лего' in words:
		await send_status('a')
	if 'лева' in words:
		await send_status('a')


	if 'назад' in words:
		await send_status('s')

	if 'вперед' in words:
		await send_status('w')
	if 'перед' in words:
		await send_status('w')


async def websock_handler(websocket, path):
	print('WS connect')
	global websocket_connections
	websocket_connections.append(websocket)
	try:
		while True:
			msg = await websocket.recv()
			print('[MSG INCOMING]', msg)
			await executor(msg)
	except websockets.exceptions.ConnectionClosedOK as e:
		pass
	websocket_connections.remove(websocket)
	print('WS disc')


async def tcp_handler(reader, writer):
	print('connected to ue')
	global tcp_connections
	connection = (reader, writer)
	tcp_connections.append(connection)
	writer.write("ping".encode())
	while True:
		data = await reader.read(100)
		if len(data) == 0:
			break
		await writer.drain()
	writer.close()
	tcp_connections.remove(connection)
	print('disconnected UE')


async def run_ws():
	await websockets.serve(websock_handler, HOST, WS_PORT)

async def run_tcp():
	await asyncio.start_server(tcp_handler, HOST, TCP_PORT, loop=loop)

def main():
	loop.create_task(run_ws())
	loop.create_task(run_tcp())
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		print("stoped")

if __name__ == '__main__':
	main()
