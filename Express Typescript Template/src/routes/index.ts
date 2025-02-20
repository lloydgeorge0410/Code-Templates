import { Request, Response, Router } from "express";
import asyncHandler from "express-async-handler";

const router = Router();

router.get(
  "/",
  asyncHandler(async (_: Request, res: Response) => {
    throw Error("test error")
    res.send("Server is healthy.");
  }),
);

export default router;
