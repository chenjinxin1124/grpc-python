from __future__ import print_function

import logging
import time
from typing import List
import random

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    answer = [0] * length

    # answer[i] 表示索引 i 左侧所有元素的乘积
    # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    # R 为右侧所有元素的乘积
    # 刚开始右边没有元素，所以 R = 1
    R = 1
    for i in reversed(range(length)):
        # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
        answer[i] = answer[i] * R
        # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
        R *= nums[i]

    return answer


def simple_test(channel):
    """简单数据，执行一次"""
    nums = [1, 2, 3, 4]
    # grpc
    start = time.time()
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.ProductExceptSelf(
        helloworld_pb2.ProductExceptSelfRequest(nums=nums)
    )
    print(response.nums)
    print(f"grpc: {time.time() - start}")

    # local
    start = time.time()
    result = productExceptSelf(nums)
    print(result)
    print(f"local: {time.time() - start}")


def complex_test(channel):
    """复杂数据，执行多次"""
    cycles = 10000
    # print(nums)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # grpc
    start = time.time()
    for _ in range(cycles):
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.ProductExceptSelf(
            helloworld_pb2.ProductExceptSelfRequest(nums=nums)
        )
        # print(response.nums)
    print(f"grpc: {time.time() - start}")

    # local
    start = time.time()
    for _ in range(cycles):
        result = productExceptSelf(nums)
        # print(result)
    print(f"local: {time.time() - start}")


def random_test(channel):
    """随机数据，执行多次，数据量大，数据范围小"""
    cycles = 1
    # 生成随机数据
    # 数据范围
    range_min = 1
    range_max = 100
    # 数据量
    nums_length = 10000
    nums = [random.randint(range_min, range_max) for _ in range(nums_length)]
    # print(nums)

    # grpc
    start = time.time()
    for _ in range(cycles):
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.ProductExceptSelf(
            helloworld_pb2.ProductExceptSelfRequest(nums=nums)
        )
        # print(response.nums)
    print(f"grpc: {time.time() - start}")

    # local
    start = time.time()
    for _ in range(cycles):
        result = productExceptSelf(nums)
        # print(result)
    print(f"local: {time.time() - start}")


def random_test2(channel):
    """随机数据，执行多次，数据量大，数据范围大"""
    cycles = 1
    # 生成随机数据
    # 数据范围
    range_min = 1000
    range_max = 10000
    # 数据量
    nums_length = 10000
    nums = [random.randint(range_min, range_max) for _ in range(nums_length)]
    # print(nums)

    # grpc
    start = time.time()
    for _ in range(cycles):
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.ProductExceptSelf(
            helloworld_pb2.ProductExceptSelfRequest(nums=nums)
        )
        # print(response.nums)
    print(f"grpc: {time.time() - start}")

    # local
    start = time.time()
    for _ in range(cycles):
        result = productExceptSelf(nums)
        # print(result)
    print(f"local: {time.time() - start}")


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        # 比较执行速度

        # 简单数据
        print("---------------------simple_test----------------------")
        simple_test(channel)
        print("---------------------simple_test----------------------")

        # 复杂数据
        print("---------------------complex_test----------------------")
        complex_test(channel)
        print("---------------------complex_test----------------------")

        # 生成随机数据
        print("---------------------random_test----------------------")
        random_test(channel)
        print("---------------------random_test----------------------")
        print("---------------------random_test2----------------------")
        random_test2(channel)
        print("---------------------random_test2----------------------")


if __name__ == "__main__":
    logging.basicConfig()
    run()
    """
    gRPC: Go
    local: Python
    ---------------------simple_test----------------------
    [24, 12, 8, 6]
    grpc: 0.001056671142578125
    [24, 12, 8, 6]
    local: 1.0013580322265625e-05
    ---------------------simple_test----------------------
    ---------------------complex_test----------------------
    grpc: 1.32623291015625
    local: 0.014175653457641602
    ---------------------complex_test----------------------
    ---------------------random_test----------------------
    grpc: 0.0015406608581542969
    local: 1.380040168762207
    ---------------------random_test----------------------
    ---------------------random_test2----------------------
    grpc: 0.0010612010955810547
    local: 5.745871543884277
    ---------------------random_test2----------------------
    """

    """
    gRPC: Python
    local: Python
    
    """
