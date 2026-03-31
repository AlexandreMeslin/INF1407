from django.shortcuts import render

# Create your views here.

# Para implementar push com http
import asyncio
from django.http import StreamingHttpResponse

async def event_stream():
    """
    Implementa push com http
    Gera mensagens SSE de forma assíncrona.
    """
    while True:
        yield f"data: Atualização em {asyncio.get_event_loop().time()}\n\n"
        await asyncio.sleep(2)

async def sse_view(request):
    """
    Implementa push com http
    Mantém conexão HTTP aberta para envio de eventos.
    """
    async def stream():
        async for msg in event_stream():
            yield msg.encode("utf-8")

    response = StreamingHttpResponse(stream(), content_type="text/event-stream")
    response["Cache-Control"] = "no-cache"
    return response
