from pathlib import Path
import gpxpy
import pandas as pd

class GpxReader:
    def __init__(self, data_dir: str='../data', output_file: str='data.parquet'):
        self.data_dir = Path(data_dir)
        self.output_file = Path(output_file)
    
    @staticmethod
    def read_gpx_track(filepath: str) -> pd.DataFrame:
        #
        gpx_file = open(filepath, 'r')
        gpx = gpxpy.parse(gpx_file)
        #
        res = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    res.append([point.latitude, point.longitude, point.elevation])
        #
        return (
            pd.DataFrame(res, columns=['latitude', 'longitude', 'elevation'])
            .assign(
                name=track.name,
            )
        )
    
    def read_all_gpx_tracks(self) -> pd.DataFrame:
        res = []
        for filepath in self.data_dir.iterdir():
            print(filepath)
            track = self.read_gpx_track(filepath)
            res.append(track)
        return pd.concat(res)
    
    def run(self):
        tracks = self.read_all_gpx_tracks()
        tracks.to_parquet(self.output_file)

r = GpxReader()
r.run()
