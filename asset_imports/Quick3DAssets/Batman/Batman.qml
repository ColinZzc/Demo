import QtQuick 2.15
import QtQuick3D 1.15

Model {
    id: defaultobject
    source: "meshes/defaultobject.mesh"

    DefaultMaterial {
        id: model001_Material001_material
        diffuseMap: Texture {
            source: "maps/Batman_V3_Cape_DS_1-4_D.tga"
            tilingModeHorizontal: Texture.Repeat
            tilingModeVertical: Texture.Repeat
        }
    }

    DefaultMaterial {
        id: model001_Material002_material
        diffuseMap: Texture {
            source: "maps/Batman_V3_Cape_DS_1-4_D.tga"
            tilingModeHorizontal: Texture.Repeat
            tilingModeVertical: Texture.Repeat
        }
    }

    DefaultMaterial {
        id: model001_Material003_material
        diffuseMap: Texture {
            source: "maps/DLC3_Batman1970_head_D.tga"
            tilingModeHorizontal: Texture.Repeat
            tilingModeVertical: Texture.Repeat
        }
    }

    DefaultMaterial {
        id: model001_Material004_material
        diffuseMap: Texture {
            source: "maps/DLC3_Batman1970_leg_D.tga"
            tilingModeHorizontal: Texture.Repeat
            tilingModeVertical: Texture.Repeat
        }
    }
    materials: [
        model001_Material001_material,
        model001_Material002_material,
        model001_Material003_material,
        model001_Material004_material
    ]
}
