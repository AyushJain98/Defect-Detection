# Surface Defect Detection System

An automated defect detection system using Computer Vision (OpenCV).
Built as part of my Smart Manufacturing engineering studies at IIITDM Jabalpur.

## What it does
- Loads an image of a manufactured surface
- Converts to grayscale for processing
- Detects edges and scratches automatically using Canny edge detection
- Highlights defects in red on the original image
- Counts total defective pixels detected

## Results
- Defective pixels detected: 4112

## Output Images
### Original vs Defects Highlighted
![Defects](surface.jpg)![Defects](defects_highlighted.jpg)

## Technologies Used
- Python
- OpenCV

## How to run
```bash
pip install opencv-python
python defect_detection.py
```
## Contour Detection
- 208 raw contours detected
- 9 real defects after noise filtering
- Each defect boxed and numbered automatically

  ## Defect Classification Results
- Total defects: 9
- Small defects: 7
- Medium defects: 2  
- Large defects: 0

![Defects Classified](defects_boxed.jpg)
