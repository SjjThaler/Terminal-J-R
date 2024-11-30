using System;
using System.IO;

class Program
{
    static void Main()
    {
        int width = 1000;
        int height = 1000;
        int radius = 300; // Radius of the circle
        int centerX = width / 2;
        int centerY = height / 2;

        // Create a raw pixel buffer (3 bytes per pixel for RGB)
        byte[] pixelData = new byte[width * height * 3];

        // Fill the pixel buffer with a circle
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                int dx = x - centerX;
                int dy = y - centerY;
                int distanceSquared = dx * dx + dy * dy;

                int index = (y * width + x) * 3;

                if (distanceSquared <= radius * radius)
                {
                    // Pixels inside the circle
                    pixelData[index] = 0;       // Blue (0 for dark blue)
                    pixelData[index + 1] = 255; // Green (255 for bright green)
                    pixelData[index + 2] = 0;   // Red (0 for no red)
                }
                else
                {
                    // Pixels outside the circle (black background)
                    pixelData[index] = 0;       // Blue
                    pixelData[index + 1] = 0;   // Green
                    pixelData[index + 2] = 0;   // Red
                }
            }
        }

        // Save the pixel data to a BMP file
        SaveBitmap("output_circle.bmp", width, height, pixelData);

        Console.WriteLine("Circle bitmap saved as output_circle.bmp");
    }

    static void SaveBitmap(string filePath, int width, int height, byte[] pixelData)
    {
        // BMP file header (14 bytes)
        byte[] fileHeader = new byte[14];
        fileHeader[0] = 0x42; // 'B'
        fileHeader[1] = 0x4D; // 'M'
        int fileSize = 14 + 40 + pixelData.Length; // Header + InfoHeader + PixelData
        BitConverter.GetBytes(fileSize).CopyTo(fileHeader, 2);
        fileHeader[10] = 54; // Pixel data offset (14 + 40)

        // BMP info header (40 bytes)
        byte[] infoHeader = new byte[40];
        BitConverter.GetBytes(40).CopyTo(infoHeader, 0); // Header size
        BitConverter.GetBytes(width).CopyTo(infoHeader, 4); // Image width
        BitConverter.GetBytes(height).CopyTo(infoHeader, 8); // Image height
        BitConverter.GetBytes((short)1).CopyTo(infoHeader, 12); // Planes
        BitConverter.GetBytes((short)24).CopyTo(infoHeader, 14); // Bits per pixel
        BitConverter.GetBytes(pixelData.Length).CopyTo(infoHeader, 20); // Image size

        // Write the headers and pixel data to the file
        using var fileStream = new FileStream(filePath, FileMode.Create, FileAccess.Write);
        fileStream.Write(fileHeader, 0, fileHeader.Length);
        fileStream.Write(infoHeader, 0, infoHeader.Length);

        // BMP stores pixels bottom-to-top, so reverse rows
        for (int y = height - 1; y >= 0; y--)
        {
            fileStream.Write(pixelData, y * width * 3, width * 3);
        }
    }
}
