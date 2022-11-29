from ciona_mesh import final_mesh
import open3d as o3d

#AMG_cells = ["MGIN1R"]
#AMG_cells = ["109"]
#AMG_cells = ["AMG1","AMG2","AMG3","AMG4","AMG5","AMG6","AMG7"]
#AMG_cells = ["99","109"]
#AMG_cells = ["152","159","161"]

cells = ["ACIN2R"]
vis_list = []
for amg_cell in cells:
    smooth_surface = final_mesh(amg_cell)
    #smooth_surfave_2 = get_smooth_cell_lowres(amg_cell)
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name=amg_cell, width=960, height=540, left=0, top=0)
    vis.add_geometry(smooth_surface)
    vis_list.append(vis)
    print ("center of the cell:")
    print (smooth_surface.get_center()+[2,34,-11])
#vis1.run()
#vis.destroy_window()
#smooth_surface_2 = get_smooth_cell("AMG2")
#vis2 = o3d.visualization.Visualizer()
#vis2.create_window(window_name='TopRight', width=960, height=540, left=0, top=0)
#vis2.add_geometry(smooth_surface_2)

#vis1.run()
#vis1.destroy_window()
#vis2.run()
#vis2.destroy_window()

#o3d.visualization.draw_geometries([smooth_surface_2],mesh_show_back_face=True)

flag = False
while True:
    for vis in vis_list:
        if not vis.poll_events():
            flag = True
        vis.update_renderer()
    if flag:
        break

    #vis2.update_geometry()
    #if not vis2.poll_events():
    #    break
    #vis2.update_renderer()
'''

AMG_cells = ["vacIN2"]
for amg_cell in AMG_cells:
    #smooth_surface = get_smooth_cell(amg_cell)
    smooth_surface = final_mesh(amg_cell)
    print (smooth_surface.get_center()) 
o3d.visualization.draw_geometries([smooth_surface],mesh_show_back_face=True)
'''