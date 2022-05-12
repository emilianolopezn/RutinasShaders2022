import math
from Modelo import *
import glm

class Triangulo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.vertices = np.array(
            [
                -0.02,0.0,0.0,1.0,  0.3,0.14,0.12,1.0,  #izquierda arriba
                -0.02,-0.15,0.0,1.0,    0.3,0.14,0.12,1.0,  #izquierda abajo
                0.02,0.0,0.0,1.0,     0.3,0.14,0.12,1.0, #derecha arriba
                0.02,-0.15,0.0,1.0,    0.3,0.14,0.12,1.0 # derecha abajo
                
            ], dtype="float32"
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.2,0.0,0.0,1.0,  0.3,0.14,0.12,1.0,  #izquierda arriba
                    0.2,-0.15,0.0,1.0,    0.3,0.14,0.12,1.0,  #izquierda abajo
                    0.24,0.0,0.0,1.0,     0.3,0.14,0.12,1.0, #derecha arriba
                    0.24,-0.15,0.0,1.0,    0.3,0.14,0.12,1.0 # derecha abajo
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices,
            np.array(
                [0.0,0.0,0.0,1.0,  0.0,1.0,0.0,1.0], dtype="float32"
            ))
        for i in range(0,361,5):
            self.vertices = np.append(self.vertices,
                np.array(
                    [0.08 * math.cos(i * math.pi/180.0),0.08 * math.sin(i * math.pi/180),0.0,1.0,  0.0,1.0,0.0,1.0]
                , dtype="float32"))
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        
        if direccion == self.ARRIBA:
           self.posicion.y  = self.posicion.y + 0.001
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.001

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 8, 74)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

