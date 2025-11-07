import subprocess

print("Training model...")
subprocess.run(["python", "model/train_model.py"])

print("Predicting sample...")
subprocess.run(["python", "model/predict.py", "Starbucks"])

print("Logging feedback...")
subprocess.run(["python", "feedback/feedback_logger.py"])
