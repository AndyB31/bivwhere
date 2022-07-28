# bivwhere
Do you want to find somewhere to camp ? Biv'where is here !

## how to use:

First build the docker image

```docker build -t bivwhere -f ./back_end/Dockerfile .```

Then run the docker image

```docker run bivwhere -p 7511:7511 ```

You can now test the API with url

```localhost:7511/analyse_coordinates?e={e}&n={n}```

By replacing {e} and {n} by Swiss LV95 coordinates.

You will get an array of the map around your points with:
 + 0 for not possible for bivouac
 + 1 for can be bivouacable
 + 2 for you can go here !
