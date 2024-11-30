using System;
using System.Drawing;
using System.Windows.Forms;

class Program
{
    static void Main()
    {
        int width = 100, height = 100;
        Bitmap bitmap = new Bitmap(width, height);

        // Create the bitmap
        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                int gray = (x + y) % 256;
                bitmap.SetPixel(x, y, Color.FromArgb(gray, gray, gray));
            }
        }

        // Display the bitmap in a form
        Form form = new Form
        {
            Text = "Bitmap Viewer",
            Width = width + 40,
            Height = height + 60
        };

        PictureBox pictureBox = new PictureBox
        {
            Image = bitmap,
            Dock = DockStyle.Fill
        };

        form.Controls.Add(pictureBox);

        Application.Run(form); // Show the form
    }
}
