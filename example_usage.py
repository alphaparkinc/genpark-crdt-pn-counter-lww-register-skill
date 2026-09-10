from client import PNCounter

def main():
    print("=== Testing CRDT PN-Counter ===")
    node1 = PNCounter("client_us")
    node2 = PNCounter("client_eu")
    
    node1.inc(50)
    node1.dec(10) # 40
    
    node2.inc(25) # 25
    
    # Merge replicas
    node1.merge(node2)
    node2.merge(node1)
    
    print(f"Node 1 Converged Value: {node1.value()}")
    print(f"Node 2 Converged Value: {node2.value()}")
    assert node1.value() == node2.value() == 65
    print("=== CRDT Verification Complete ===")

if __name__ == "__main__":
    main()
