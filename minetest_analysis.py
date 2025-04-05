import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict
import json
import time

@dataclass
class PerformanceMetrics:
    fps: float
    view_distance: int
    particle_count: int
    memory_usage: float
    timestamp: float

class MinetestAnalyzer:
    def __init__(self):
        self.metrics_history: List[PerformanceMetrics] = []
        
    def record_metrics(self, fps: float, view_distance: int, 
                      particle_count: int, memory_usage: float):
        metrics = PerformanceMetrics(
            fps=fps,
            view_distance=view_distance,
            particle_count=particle_count,
            memory_usage=memory_usage,
            timestamp=time.time()
        )
        self.metrics_history.append(metrics)
        
    def analyze_performance(self) -> Dict:
        if not self.metrics_history:
            return {"error": "Нет данных для анализа"}
            
        fps_values = [m.fps for m in self.metrics_history]
        memory_values = [m.memory_usage for m in self.metrics_history]
        
        return {
            "avg_fps": float(np.mean(fps_values)),
            "min_fps": float(np.min(fps_values)),
            "max_fps": float(np.max(fps_values)),
            "avg_memory": float(np.mean(memory_values)),
            "memory_trend": float(np.polyfit(range(len(memory_values)), memory_values, 1)[0])
        }
        
    def plot_performance(self, save_path: str = None):
        if not self.metrics_history:
            print("Нет данных для визуализации")
            return
            
        timestamps = [m.timestamp - self.metrics_history[0].timestamp 
                     for m in self.metrics_history]
        fps_values = [m.fps for m in self.metrics_history]
        memory_values = [m.memory_usage for m in self.metrics_history]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        ax1.plot(timestamps, fps_values, 'b-', label='FPS')
        ax1.set_ylabel('FPS')
        ax1.set_title('Производительность Minetest')
        ax1.grid(True)
        ax1.legend()
        
        ax2.plot(timestamps, memory_values, 'r-', label='Память (МБ)')
        ax2.set_xlabel('Время (сек)')
        ax2.set_ylabel('Память (МБ)')
        ax2.grid(True)
        ax2.legend()
        
        if save_path:
            plt.savefig(save_path)
        plt.show()

def calculate_optimal_view_distance(fps_history: List[float], 
                                 view_distances: List[int]) -> int:

    if len(fps_history) != len(view_distances):
        raise ValueError("Количество измерений FPS должно совпадать с количеством дистанций")
        
    fps_threshold = np.mean(fps_history) * 0.9  
    
    for fps, distance in zip(fps_history, view_distances):
        if fps < fps_threshold:
            return distance - 1
            
    return view_distances[-1]

if __name__ == "__main__":
    analyzer = MinetestAnalyzer()
    
    base_fps = 120  
    base_memory = 1024 
    base_particles = 5000 
    
    for i in range(20):  
        fps_variation = np.random.normal(0, 5) 
        current_fps = base_fps - (i * 2) + fps_variation 
        
        memory_growth = np.random.normal(50, 10)  
        current_memory = base_memory + (i * memory_growth)
        
        particle_variation = np.random.normal(200, 50)
        current_particles = base_particles + (i * particle_variation)
        
        analyzer.record_metrics(
            fps=max(1, current_fps), 
            view_distance=100 + i * 5, 
            particle_count=int(max(0, current_particles)),  
            memory_usage=current_memory
        )
        
        time.sleep(0.1)
    
    # Анализ и визуализация
    results = analyzer.analyze_performance()
    print("Результаты анализа:", json.dumps(results, indent=2, ensure_ascii=False))
    analyzer.plot_performance("minetest_performance.png") 