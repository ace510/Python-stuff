#version 330

// (x,y) position passed in
in vec2 in_pos;

//output the color to the fragment shader
out vec4 color;

void main() {
    //set the RGB + Alpha color
    color = vec4(1,1,1,1);
    //set the position (x, y) as well as z? and w? shouldn't really affect
    gl_Position = vec4(in_pos, 0.0, 1);
}