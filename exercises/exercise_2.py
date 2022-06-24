def int32_to_ip(int32):
    return f"{int32 // 256 // 256 // 256}.{int32 // 256 // 256 % 256}.{int32 // 256 % 256}.{int32 % 256}"

