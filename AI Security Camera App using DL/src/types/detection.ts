export interface Detection {
  bbox: number[];
  class: string;
  score: number;
  timestamp: number;
}

export interface MotionData {
  isMoving: boolean;
  intensity: number;
}