#*--------------------------------------------------
#* facade.py
#* excerpt from https://refactoring.guru/design-patterns/facade/python/example
#*--------------------------------------------------

from __future__ import annotations


class Facade:
    def __init__(self, h264_decode: H264, h265_decode: H265) -> None:
        self._h264_decode = h264_decode or H264()
        self._h265_decode = h265_decode or H265()

    def operation(self) -> str:
        results = []
        results.append("Facade inicializa el sistema y prepara los videos:")
        results.append(self._h264_decode.preparar_video())
        results.append(self._h265_decode.preparar_video())
        return "\n".join(results)


class H264:
    def preparar_video(self) -> str:
        return "Video en H.264 aceptado."

class H265:
    def preparar_video(self) -> str:
        return "Video en H.265 aceptado."

def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":
    h264_decode = H264()
    h265_decode= H265()
    facade = Facade(h264_decode, h265_decode)
    client_code(facade)
    print("\n")
