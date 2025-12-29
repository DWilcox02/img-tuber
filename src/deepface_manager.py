from deepface import DeepFace


class DeepfaceManager:

    def __init__(self):
        pass

    def check_emotion(self, frame):
        demography = DeepFace.analyze(frame, ["emotion"])[0]
        self.format_emotion_print(demography)

    def format_emotion_print(self, demography):
        # demography structure: 
        # {"emotion": {"angry": 0.01, "disgust": 0.0, ...}, "dominant_emotion": "neutral"}
        
        emotions = demography["emotion"]
        
        print(f"ANALYSIS: {demography['dominant_emotion'].upper()}")
        print(f"  anger:    {round(emotions['angry'], 2)}%")
        print(f"  disgust:  {round(emotions['disgust'], 2)}%")
        print(f"  fear:     {round(emotions['fear'], 2)}%")
        print(f"  happy:    {round(emotions['happy'], 2)}%")
        print(f"  neutral:  {round(emotions['neutral'], 2)}%")
        print(f"  sad:      {round(emotions['sad'], 2)}%")
        print(f"  surprise: {round(emotions['surprise'], 2)}%")